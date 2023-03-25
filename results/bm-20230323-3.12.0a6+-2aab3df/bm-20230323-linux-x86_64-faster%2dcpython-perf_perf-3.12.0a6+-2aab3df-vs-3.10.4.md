
# Results vs. 3.10.4

- fork: faster-cpython
- ref: perf_perf
- machine: linux-x86_64
- commit hash: 2aab3df
- commit date: 2023-03-23
- overall geometric mean: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 271 ms: 1.24x faster                                                  |
| chameleon      | 9.13 ms                                                             | 7.07 ms: 1.29x faster                                                 |
| docutils       | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                                |
| html5lib       | 86.4 ms                                                             | 68.3 ms: 1.26x faster                                                 |
| tornado_http   | 129 ms                                                              | 104 ms: 1.24x faster                                                  |
| Geometric mean | (ref)                                                               | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 89.0 ms: 1.64x faster                                                 |
| float          | 110 ms                                                              | 79.0 ms: 1.39x faster                                                 |
| pidigits       | 190 ms                                                              | 189 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                               | 1.32x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 145 ms: 1.22x faster                                                  |
| regex_v8       | 24.9 ms                                                             | 22.7 ms: 1.10x faster                                                 |
| regex_dna      | 213 ms                                                              | 206 ms: 1.03x faster                                                  |
| regex_effbot   | 3.22 ms                                                             | 3.40 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                               | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 13.7 ms                                                             | 9.78 ms: 1.40x faster                                                 |
| pickle_pure_python   | 457 us                                                              | 337 us: 1.36x faster                                                  |
| unpickle_pure_python | 300 us                                                              | 238 us: 1.26x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 60.6 ms: 1.23x faster                                                 |
| json_loads           | 29.3 us                                                             | 24.4 us: 1.20x faster                                                 |
| pickle_list          | 4.73 us                                                             | 4.10 us: 1.15x faster                                                 |
| xml_etree_generate   | 94.9 ms                                                             | 84.1 ms: 1.13x faster                                                 |
| unpickle             | 15.0 us                                                             | 13.6 us: 1.10x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                              | 102 ms: 1.09x faster                                                  |
| xml_etree_parse      | 164 ms                                                              | 150 ms: 1.09x faster                                                  |
| unpickle_list        | 4.94 us                                                             | 5.20 us: 1.05x slower                                                 |
| pickle_dict          | 27.8 us                                                             | 30.5 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.14x faster                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.52 ms: 1.49x faster                                                 |
| python_startup_no_site | 5.80 ms                                                             | 6.88 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.12x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.6 ms: 1.38x faster                                                 |
| genshi_text     | 30.4 ms                                                             | 24.5 ms: 1.24x faster                                                 |
| genshi_xml      | 64.3 ms                                                             | 52.2 ms: 1.23x faster                                                 |
| django_template | 45.8 ms                                                             | 39.1 ms: 1.17x faster                                                 |
| Geometric mean  | (ref)                                                               | 1.26x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-perf_perf-3.12.0a6+-2aab3df |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.4 ms: 2.58x faster                                                 |
| asyncio_tcp             | 922 ms                                                              | 522 ms: 1.77x faster                                                  |
| nbody                   | 146 ms                                                              | 89.0 ms: 1.64x faster                                                 |
| deltablue               | 7.30 ms                                                             | 4.47 ms: 1.63x faster                                                 |
| crypto_pyaes            | 117 ms                                                              | 74.8 ms: 1.56x faster                                                 |
| scimark_sor             | 198 ms                                                              | 127 ms: 1.56x faster                                                  |
| unpack_sequence         | 65.6 ns                                                             | 42.7 ns: 1.54x faster                                                 |
| scimark_monte_carlo     | 109 ms                                                              | 71.9 ms: 1.51x faster                                                 |
| chaos                   | 106 ms                                                              | 70.3 ms: 1.51x faster                                                 |
| scimark_lu              | 160 ms                                                              | 108 ms: 1.49x faster                                                  |
| python_startup          | 14.1 ms                                                             | 9.52 ms: 1.49x faster                                                 |
| scimark_fft             | 425 ms                                                              | 302 ms: 1.41x faster                                                  |
| pyflate                 | 671 ms                                                              | 478 ms: 1.40x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 9.78 ms: 1.40x faster                                                 |
| go                      | 226 ms                                                              | 161 ms: 1.40x faster                                                  |
| raytrace                | 470 ms                                                              | 337 ms: 1.40x faster                                                  |
| spectral_norm           | 150 ms                                                              | 108 ms: 1.39x faster                                                  |
| float                   | 110 ms                                                              | 79.0 ms: 1.39x faster                                                 |
| mako                    | 14.7 ms                                                             | 10.6 ms: 1.38x faster                                                 |
| richards                | 74.2 ms                                                             | 54.6 ms: 1.36x faster                                                 |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.14 ms: 1.36x faster                                                 |
| pickle_pure_python      | 457 us                                                              | 337 us: 1.36x faster                                                  |
| hexiom                  | 9.50 ms                                                             | 7.09 ms: 1.34x faster                                                 |
| logging_silent          | 169 ns                                                              | 130 ns: 1.30x faster                                                  |
| pycparser               | 1.53 sec                                                            | 1.18 sec: 1.30x faster                                                |
| chameleon               | 9.13 ms                                                             | 7.07 ms: 1.29x faster                                                 |
| async_tree_io           | 1.78 sec                                                            | 1.39 sec: 1.29x faster                                                |
| html5lib                | 86.4 ms                                                             | 68.3 ms: 1.26x faster                                                 |
| unpickle_pure_python    | 300 us                                                              | 238 us: 1.26x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 41.2 us: 1.26x faster                                                 |
| async_tree_none         | 713 ms                                                              | 568 ms: 1.25x faster                                                  |
| fannkuch                | 485 ms                                                              | 387 ms: 1.25x faster                                                  |
| thrift                  | 1.04 ms                                                             | 830 us: 1.25x faster                                                  |
| async_tree_memoization  | 853 ms                                                              | 684 ms: 1.25x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.66 ms: 1.25x faster                                                 |
| pprint_pformat          | 1.98 sec                                                            | 1.59 sec: 1.25x faster                                                |
| genshi_text             | 30.4 ms                                                             | 24.5 ms: 1.24x faster                                                 |
| 2to3                    | 336 ms                                                              | 271 ms: 1.24x faster                                                  |
| tornado_http            | 129 ms                                                              | 104 ms: 1.24x faster                                                  |
| gunicorn                | 1.43 ms                                                             | 1.16 ms: 1.24x faster                                                 |
| pprint_safe_repr        | 953 ms                                                              | 770 ms: 1.24x faster                                                  |
| aiohttp                 | 1.35 ms                                                             | 1.09 ms: 1.24x faster                                                 |
| xml_etree_process       | 74.8 ms                                                             | 60.6 ms: 1.23x faster                                                 |
| genshi_xml              | 64.3 ms                                                             | 52.2 ms: 1.23x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                             | 1.99 ms: 1.23x faster                                                 |
| regex_compile           | 177 ms                                                              | 145 ms: 1.22x faster                                                  |
| json_loads              | 29.3 us                                                             | 24.4 us: 1.20x faster                                                 |
| async_tree_cpu_io_mixed | 944 ms                                                              | 793 ms: 1.19x faster                                                  |
| docutils                | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                                |
| django_template         | 45.8 ms                                                             | 39.1 ms: 1.17x faster                                                 |
| nqueens                 | 98.8 ms                                                             | 84.6 ms: 1.17x faster                                                 |
| deepcopy                | 438 us                                                              | 377 us: 1.16x faster                                                  |
| json                    | 5.41 ms                                                             | 4.67 ms: 1.16x faster                                                 |
| pickle_list             | 4.73 us                                                             | 4.10 us: 1.15x faster                                                 |
| mypy2                   | 432 ms                                                              | 378 ms: 1.14x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 837 us: 1.14x faster                                                  |
| coroutines              | 31.8 ms                                                             | 28.0 ms: 1.13x faster                                                 |
| sqlite_synth            | 2.97 us                                                             | 2.62 us: 1.13x faster                                                 |
| deepcopy_reduce         | 3.80 us                                                             | 3.35 us: 1.13x faster                                                 |
| xml_etree_generate      | 94.9 ms                                                             | 84.1 ms: 1.13x faster                                                 |
| sqlalchemy_declarative  | 166 ms                                                              | 148 ms: 1.12x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                             | 58.5 ms: 1.12x faster                                                 |
| sqlglot_normalize       | 135 ms                                                              | 121 ms: 1.11x faster                                                  |
| logging_format          | 9.07 us                                                             | 8.20 us: 1.11x faster                                                 |
| create_gc_cycles        | 1.64 ms                                                             | 1.48 ms: 1.10x faster                                                 |
| unpickle                | 15.0 us                                                             | 13.6 us: 1.10x faster                                                 |
| regex_v8                | 24.9 ms                                                             | 22.7 ms: 1.10x faster                                                 |
| logging_simple          | 8.21 us                                                             | 7.48 us: 1.10x faster                                                 |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.09x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 102 ms: 1.09x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 69.9 ms: 1.09x faster                                                 |
| xml_etree_parse         | 164 ms                                                              | 150 ms: 1.09x faster                                                  |
| djangocms               | 36.3 us                                                             | 33.4 us: 1.09x faster                                                 |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.5 ms: 1.09x faster                                                 |
| sympy_integrate         | 24.3 ms                                                             | 22.4 ms: 1.09x faster                                                 |
| sympy_expand            | 540 ms                                                              | 501 ms: 1.08x faster                                                  |
| sympy_str               | 328 ms                                                              | 311 ms: 1.06x faster                                                  |
| comprehensions          | 27.3 us                                                             | 26.0 us: 1.05x faster                                                 |
| pathlib                 | 19.8 ms                                                             | 19.0 ms: 1.04x faster                                                 |
| mdp                     | 2.75 sec                                                            | 2.65 sec: 1.04x faster                                                |
| regex_dna               | 213 ms                                                              | 206 ms: 1.03x faster                                                  |
| sympy_sum               | 185 ms                                                              | 179 ms: 1.03x faster                                                  |
| telco                   | 6.67 ms                                                             | 6.58 ms: 1.01x faster                                                 |
| pidigits                | 190 ms                                                              | 189 ms: 1.00x faster                                                  |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                 |
| async_generators        | 420 ms                                                              | 436 ms: 1.04x slower                                                  |
| unpickle_list           | 4.94 us                                                             | 5.20 us: 1.05x slower                                                 |
| regex_effbot            | 3.22 ms                                                             | 3.40 ms: 1.06x slower                                                 |
| pickle_dict             | 27.8 us                                                             | 30.5 us: 1.10x slower                                                 |
| python_startup_no_site  | 5.80 ms                                                             | 6.88 ms: 1.19x slower                                                 |
| gc_traversal            | 3.53 ms                                                             | 4.32 ms: 1.23x slower                                                 |
| dask                    | 437 ms                                                              | 557 ms: 1.28x slower                                                  |
| coverage                | 70.6 ms                                                             | 103 ms: 1.46x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.20x faster                                                          |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
