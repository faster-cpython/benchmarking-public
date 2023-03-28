
# Results vs. 3.10.4

- fork: python
- ref: 72f00f420afaba3bc873
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 282 ms: 1.25x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.50 ms: 1.28x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                      |
| html5lib       | 96.3 ms                                                      | 70.8 ms: 1.36x faster                                                       |
| tornado_http   | 151 ms                                                       | 122 ms: 1.24x faster                                                        |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.8 ms: 1.48x faster                                                       |
| nbody          | 132 ms                                                       | 89.8 ms: 1.47x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 155 ms: 1.23x faster                                                        |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 24.1 ms: 1.08x faster                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.17 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 77.6 ms                                                      | 55.7 ms: 1.39x faster                                                       |
| pickle_pure_python   | 451 us                                                       | 324 us: 1.39x faster                                                        |
| unpickle_pure_python | 318 us                                                       | 235 us: 1.35x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.22x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 79.9 ms: 1.18x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 13.3 ms: 1.08x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 153 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 105 ms: 1.04x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.97 us: 1.04x faster                                                       |
| pickle               | 10.1 us                                                      | 9.79 us: 1.04x faster                                                       |
| unpickle_list        | 4.73 us                                                      | 4.66 us: 1.02x faster                                                       |
| unpickle             | 13.3 us                                                      | 13.4 us: 1.01x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 30.9 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.6 ms: 1.08x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.67 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                       |
| django_template | 52.0 ms                                                      | 40.4 ms: 1.29x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 25.1 ms: 1.26x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 56.9 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 4.05 ms: 1.86x faster                                                       |
| go                      | 264 ms                                                       | 159 ms: 1.66x faster                                                        |
| pyflate                 | 731 ms                                                       | 440 ms: 1.66x faster                                                        |
| logging_silent          | 165 ns                                                       | 99.8 ns: 1.65x faster                                                       |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.62x faster                                                        |
| raytrace                | 491 ms                                                       | 305 ms: 1.61x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.44 ms: 1.60x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 69.3 ms: 1.57x faster                                                       |
| richards                | 73.9 ms                                                      | 49.5 ms: 1.49x faster                                                       |
| float                   | 109 ms                                                       | 73.8 ms: 1.48x faster                                                       |
| nbody                   | 132 ms                                                       | 89.8 ms: 1.47x faster                                                       |
| chaos                   | 108 ms                                                       | 73.9 ms: 1.46x faster                                                       |
| scimark_lu              | 164 ms                                                       | 116 ms: 1.42x faster                                                        |
| spectral_norm           | 138 ms                                                       | 98.9 ms: 1.39x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 55.7 ms: 1.39x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 324 us: 1.39x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 85.4 ms: 1.39x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                      |
| html5lib                | 96.3 ms                                                      | 70.8 ms: 1.36x faster                                                       |
| async_tree_none         | 698 ms                                                       | 516 ms: 1.35x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 235 us: 1.35x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 7.12 ms: 1.34x faster                                                       |
| logging_simple          | 9.24 us                                                      | 6.91 us: 1.34x faster                                                       |
| mako                    | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 769 ms: 1.33x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.60 sec: 1.33x faster                                                      |
| deepcopy_memo           | 49.2 us                                                      | 37.1 us: 1.33x faster                                                       |
| async_generators        | 419 ms                                                       | 316 ms: 1.32x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 624 ms: 1.32x faster                                                        |
| thrift                  | 1.23 ms                                                      | 933 us: 1.31x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 45.8 ns: 1.30x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.71 us: 1.29x faster                                                       |
| django_template         | 52.0 ms                                                      | 40.4 ms: 1.29x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.29 sec: 1.28x faster                                                      |
| chameleon               | 9.62 ms                                                      | 7.50 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 746 ms: 1.28x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.04 ms: 1.26x faster                                                       |
| genshi_text             | 31.7 ms                                                      | 25.1 ms: 1.26x faster                                                       |
| 2to3                    | 352 ms                                                       | 282 ms: 1.25x faster                                                        |
| aiohttp                 | 1.18 ms                                                      | 949 us: 1.24x faster                                                        |
| scimark_fft             | 359 ms                                                       | 290 ms: 1.24x faster                                                        |
| tornado_http            | 151 ms                                                       | 122 ms: 1.24x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 930 us: 1.23x faster                                                        |
| regex_compile           | 191 ms                                                       | 155 ms: 1.23x faster                                                        |
| sqlalchemy_declarative  | 188 ms                                                       | 154 ms: 1.22x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.8 us: 1.22x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 123 ms: 1.20x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                      |
| dulwich_log             | 80.5 ms                                                      | 67.5 ms: 1.19x faster                                                       |
| deepcopy                | 457 us                                                       | 383 us: 1.19x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 59.2 ms: 1.18x faster                                                       |
| sqlite_synth            | 2.96 us                                                      | 2.51 us: 1.18x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 79.9 ms: 1.18x faster                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 2.29 ms: 1.17x faster                                                       |
| regex_dna               | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| sqlalchemy_imperative   | 22.9 ms                                                      | 19.6 ms: 1.17x faster                                                       |
| nqueens                 | 114 ms                                                       | 98.2 ms: 1.16x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 1.94 ms: 1.15x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.41 us: 1.15x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 993 us: 1.15x faster                                                        |
| dask                    | 478 ms                                                       | 417 ms: 1.15x faster                                                        |
| json                    | 5.94 ms                                                      | 5.19 ms: 1.15x faster                                                       |
| sympy_expand            | 603 ms                                                       | 536 ms: 1.13x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.61 ms: 1.12x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.1 ms: 1.12x faster                                                       |
| genshi_xml              | 63.5 ms                                                      | 56.9 ms: 1.12x faster                                                       |
| pathlib                 | 21.3 ms                                                      | 19.2 ms: 1.11x faster                                                       |
| pylint                  | 562 ms                                                       | 511 ms: 1.10x faster                                                        |
| sympy_sum               | 193 ms                                                       | 176 ms: 1.10x faster                                                        |
| sympy_str               | 358 ms                                                       | 327 ms: 1.09x faster                                                        |
| meteor_contest          | 142 ms                                                       | 130 ms: 1.09x faster                                                        |
| coroutines              | 30.6 ms                                                      | 28.2 ms: 1.08x faster                                                       |
| regex_v8                | 26.0 ms                                                      | 24.1 ms: 1.08x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.6 ms: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 13.3 ms: 1.08x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.75 sec: 1.07x faster                                                      |
| fannkuch                | 496 ms                                                       | 469 ms: 1.06x faster                                                        |
| generators              | 57.0 ms                                                      | 54.2 ms: 1.05x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 750 ms: 1.05x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 153 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 105 ms: 1.04x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.97 us: 1.04x faster                                                       |
| pickle                  | 10.1 us                                                      | 9.79 us: 1.04x faster                                                       |
| telco                   | 7.14 ms                                                      | 7.01 ms: 1.02x faster                                                       |
| unpickle_list           | 4.73 us                                                      | 4.66 us: 1.02x faster                                                       |
| unpickle                | 13.3 us                                                      | 13.4 us: 1.01x slower                                                       |
| comprehensions          | 27.3 us                                                      | 28.3 us: 1.04x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.67 ms: 1.05x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 30.9 us: 1.05x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.17 ms: 1.06x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.70 ms: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.22x faster                                                                |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage, flaskblogging
