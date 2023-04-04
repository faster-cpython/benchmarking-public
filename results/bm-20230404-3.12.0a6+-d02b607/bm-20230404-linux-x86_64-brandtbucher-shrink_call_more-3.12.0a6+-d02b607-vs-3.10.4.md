
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_call_more
- machine: linux-x86_64
- commit hash: d02b607
- commit date: 2023-04-04
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 251 ms: 1.34x faster                                                     |
| chameleon      | 9.13 ms                                                             | 6.67 ms: 1.37x faster                                                    |
| docutils       | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                   |
| html5lib       | 86.4 ms                                                             | 60.8 ms: 1.42x faster                                                    |
| tornado_http   | 129 ms                                                              | 90.8 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                               | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.1 ms: 1.66x faster                                                    |
| float          | 110 ms                                                              | 74.1 ms: 1.48x faster                                                    |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                               | 1.35x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 132 ms: 1.34x faster                                                     |
| regex_v8       | 24.9 ms                                                             | 21.7 ms: 1.15x faster                                                    |
| regex_dna      | 213 ms                                                              | 205 ms: 1.04x faster                                                     |
| regex_effbot   | 3.22 ms                                                             | 3.69 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                               | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 284 us: 1.61x faster                                                     |
| unpickle_pure_python | 300 us                                                              | 199 us: 1.51x faster                                                     |
| json_dumps           | 13.7 ms                                                             | 9.49 ms: 1.44x faster                                                    |
| xml_etree_process    | 74.8 ms                                                             | 56.4 ms: 1.33x faster                                                    |
| json_loads           | 29.3 us                                                             | 24.3 us: 1.21x faster                                                    |
| xml_etree_generate   | 94.9 ms                                                             | 82.1 ms: 1.16x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                              | 99.9 ms: 1.11x faster                                                    |
| unpickle             | 15.0 us                                                             | 13.4 us: 1.11x faster                                                    |
| xml_etree_parse      | 164 ms                                                              | 148 ms: 1.11x faster                                                     |
| pickle_list          | 4.73 us                                                             | 4.36 us: 1.08x faster                                                    |
| pickle               | 10.2 us                                                             | 10.5 us: 1.03x slower                                                    |
| unpickle_list        | 4.94 us                                                             | 5.17 us: 1.05x slower                                                    |
| pickle_dict          | 27.8 us                                                             | 31.4 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.78 ms: 1.61x faster                                                    |
| python_startup_no_site | 5.80 ms                                                             | 6.49 ms: 1.12x slower                                                    |
| Geometric mean         | (ref)                                                               | 1.20x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.2 ms: 1.45x faster                                                    |
| genshi_text     | 30.4 ms                                                             | 21.2 ms: 1.43x faster                                                    |
| django_template | 45.8 ms                                                             | 33.8 ms: 1.36x faster                                                    |
| genshi_xml      | 64.3 ms                                                             | 48.0 ms: 1.34x faster                                                    |
| Geometric mean  | (ref)                                                               | 1.39x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.3 ms: 2.59x faster                                                    |
| deltablue               | 7.30 ms                                                             | 3.25 ms: 2.25x faster                                                    |
| asyncio_tcp             | 922 ms                                                              | 500 ms: 1.84x faster                                                     |
| logging_silent          | 169 ns                                                              | 98.3 ns: 1.72x faster                                                    |
| richards                | 74.2 ms                                                             | 43.5 ms: 1.70x faster                                                    |
| scimark_sor             | 198 ms                                                              | 116 ms: 1.70x faster                                                     |
| raytrace                | 470 ms                                                              | 279 ms: 1.68x faster                                                     |
| nbody                   | 146 ms                                                              | 88.1 ms: 1.66x faster                                                    |
| go                      | 226 ms                                                              | 137 ms: 1.65x faster                                                     |
| python_startup          | 14.1 ms                                                             | 8.78 ms: 1.61x faster                                                    |
| chaos                   | 106 ms                                                              | 65.8 ms: 1.61x faster                                                    |
| pickle_pure_python      | 457 us                                                              | 284 us: 1.61x faster                                                     |
| spectral_norm           | 150 ms                                                              | 94.5 ms: 1.59x faster                                                    |
| scimark_monte_carlo     | 109 ms                                                              | 68.6 ms: 1.58x faster                                                    |
| crypto_pyaes            | 117 ms                                                              | 75.3 ms: 1.55x faster                                                    |
| unpack_sequence         | 65.6 ns                                                             | 42.4 ns: 1.55x faster                                                    |
| hexiom                  | 9.50 ms                                                             | 6.16 ms: 1.54x faster                                                    |
| pyflate                 | 671 ms                                                              | 441 ms: 1.52x faster                                                     |
| unpickle_pure_python    | 300 us                                                              | 199 us: 1.51x faster                                                     |
| deepcopy_memo           | 51.8 us                                                             | 34.4 us: 1.51x faster                                                    |
| scimark_lu              | 160 ms                                                              | 108 ms: 1.48x faster                                                     |
| float                   | 110 ms                                                              | 74.1 ms: 1.48x faster                                                    |
| mako                    | 14.7 ms                                                             | 10.2 ms: 1.45x faster                                                    |
| json_dumps              | 13.7 ms                                                             | 9.49 ms: 1.44x faster                                                    |
| genshi_text             | 30.4 ms                                                             | 21.2 ms: 1.43x faster                                                    |
| logging_format          | 9.07 us                                                             | 6.34 us: 1.43x faster                                                    |
| logging_simple          | 8.21 us                                                             | 5.76 us: 1.43x faster                                                    |
| sqlglot_parse           | 2.07 ms                                                             | 1.45 ms: 1.42x faster                                                    |
| html5lib                | 86.4 ms                                                             | 60.8 ms: 1.42x faster                                                    |
| tornado_http            | 129 ms                                                              | 90.8 ms: 1.42x faster                                                    |
| sqlglot_transpile       | 2.45 ms                                                             | 1.75 ms: 1.40x faster                                                    |
| pycparser               | 1.53 sec                                                            | 1.09 sec: 1.40x faster                                                   |
| pprint_pformat          | 1.98 sec                                                            | 1.43 sec: 1.38x faster                                                   |
| async_tree_io           | 1.78 sec                                                            | 1.29 sec: 1.38x faster                                                   |
| scimark_fft             | 425 ms                                                              | 309 ms: 1.37x faster                                                     |
| pprint_safe_repr        | 953 ms                                                              | 695 ms: 1.37x faster                                                     |
| chameleon               | 9.13 ms                                                             | 6.67 ms: 1.37x faster                                                    |
| async_tree_none         | 713 ms                                                              | 521 ms: 1.37x faster                                                     |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.13 ms: 1.36x faster                                                    |
| django_template         | 45.8 ms                                                             | 33.8 ms: 1.36x faster                                                    |
| coroutines              | 31.8 ms                                                             | 23.5 ms: 1.35x faster                                                    |
| async_tree_memoization  | 853 ms                                                              | 635 ms: 1.34x faster                                                     |
| genshi_xml              | 64.3 ms                                                             | 48.0 ms: 1.34x faster                                                    |
| regex_compile           | 177 ms                                                              | 132 ms: 1.34x faster                                                     |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                    |
| 2to3                    | 336 ms                                                              | 251 ms: 1.34x faster                                                     |
| xml_etree_process       | 74.8 ms                                                             | 56.4 ms: 1.33x faster                                                    |
| gunicorn                | 1.43 ms                                                             | 1.08 ms: 1.33x faster                                                    |
| thrift                  | 1.04 ms                                                             | 783 us: 1.32x faster                                                     |
| deepcopy                | 438 us                                                              | 333 us: 1.32x faster                                                     |
| mypy2                   | 432 ms                                                              | 331 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed | 944 ms                                                              | 734 ms: 1.29x faster                                                     |
| sqlglot_normalize       | 135 ms                                                              | 105 ms: 1.28x faster                                                     |
| deepcopy_reduce         | 3.80 us                                                             | 2.99 us: 1.27x faster                                                    |
| sqlglot_optimize        | 65.3 ms                                                             | 51.6 ms: 1.27x faster                                                    |
| docutils                | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                   |
| fannkuch                | 485 ms                                                              | 388 ms: 1.25x faster                                                     |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.22x faster                                                     |
| bench_thread_pool       | 954 us                                                              | 790 us: 1.21x faster                                                     |
| json_loads              | 29.3 us                                                             | 24.3 us: 1.21x faster                                                    |
| dulwich_log             | 76.3 ms                                                             | 63.8 ms: 1.20x faster                                                    |
| nqueens                 | 98.8 ms                                                             | 82.7 ms: 1.20x faster                                                    |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.7 ms: 1.19x faster                                                    |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.19x faster                                                    |
| json                    | 5.41 ms                                                             | 4.61 ms: 1.17x faster                                                    |
| sympy_expand            | 540 ms                                                              | 464 ms: 1.16x faster                                                     |
| xml_etree_generate      | 94.9 ms                                                             | 82.1 ms: 1.16x faster                                                    |
| sympy_str               | 328 ms                                                              | 284 ms: 1.15x faster                                                     |
| regex_v8                | 24.9 ms                                                             | 21.7 ms: 1.15x faster                                                    |
| comprehensions          | 27.3 us                                                             | 23.8 us: 1.14x faster                                                    |
| djangocms               | 36.3 us                                                             | 32.1 us: 1.13x faster                                                    |
| sqlite_synth            | 2.97 us                                                             | 2.66 us: 1.12x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                              | 99.9 ms: 1.11x faster                                                    |
| unpickle                | 15.0 us                                                             | 13.4 us: 1.11x faster                                                    |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                                     |
| create_gc_cycles        | 1.64 ms                                                             | 1.48 ms: 1.11x faster                                                    |
| xml_etree_parse         | 164 ms                                                              | 148 ms: 1.11x faster                                                     |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                                     |
| pathlib                 | 19.8 ms                                                             | 18.0 ms: 1.10x faster                                                    |
| pickle_list             | 4.73 us                                                             | 4.36 us: 1.08x faster                                                    |
| mdp                     | 2.75 sec                                                            | 2.55 sec: 1.08x faster                                                   |
| regex_dna               | 213 ms                                                              | 205 ms: 1.04x faster                                                     |
| telco                   | 6.67 ms                                                             | 6.57 ms: 1.02x faster                                                    |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                     |
| async_generators        | 420 ms                                                              | 417 ms: 1.01x faster                                                     |
| pickle                  | 10.2 us                                                             | 10.5 us: 1.03x slower                                                    |
| unpickle_list           | 4.94 us                                                             | 5.17 us: 1.05x slower                                                    |
| python_startup_no_site  | 5.80 ms                                                             | 6.49 ms: 1.12x slower                                                    |
| pickle_dict             | 27.8 us                                                             | 31.4 us: 1.13x slower                                                    |
| regex_effbot            | 3.22 ms                                                             | 3.69 ms: 1.14x slower                                                    |
| dask                    | 437 ms                                                              | 510 ms: 1.17x slower                                                     |
| gc_traversal            | 3.53 ms                                                             | 4.32 ms: 1.22x slower                                                    |
| coverage                | 70.6 ms                                                             | 96.1 ms: 1.36x slower                                                    |
| Geometric mean          | (ref)                                                               | 1.29x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
