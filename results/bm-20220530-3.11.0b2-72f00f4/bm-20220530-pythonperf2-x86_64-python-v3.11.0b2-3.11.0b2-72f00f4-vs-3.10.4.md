
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b2
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 282 ms: 1.25x faster                                             |
| chameleon      | 9.62 ms                                                      | 7.52 ms: 1.28x faster                                            |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                           |
| html5lib       | 96.3 ms                                                      | 70.5 ms: 1.37x faster                                            |
| tornado_http   | 151 ms                                                       | 117 ms: 1.28x faster                                             |
| Geometric mean | (ref)                                                        | 1.28x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.8 ms: 1.48x faster                                            |
| nbody          | 132 ms                                                       | 96.9 ms: 1.36x faster                                            |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                        | 1.30x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 157 ms: 1.22x faster                                             |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                             |
| regex_v8       | 26.0 ms                                                      | 24.1 ms: 1.08x faster                                            |
| regex_effbot   | 2.99 ms                                                      | 3.11 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.10x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 451 us                                                       | 320 us: 1.41x faster                                             |
| xml_etree_process    | 77.6 ms                                                      | 55.8 ms: 1.39x faster                                            |
| unpickle_pure_python | 318 us                                                       | 234 us: 1.36x faster                                             |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                            |
| xml_etree_generate   | 94.1 ms                                                      | 79.0 ms: 1.19x faster                                            |
| json_dumps           | 14.3 ms                                                      | 13.3 ms: 1.07x faster                                            |
| pickle_list          | 4.11 us                                                      | 3.86 us: 1.07x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 153 ms: 1.04x faster                                             |
| pickle               | 10.1 us                                                      | 9.77 us: 1.04x faster                                            |
| unpickle_list        | 4.73 us                                                      | 4.57 us: 1.03x faster                                            |
| xml_etree_iterparse  | 109 ms                                                       | 106 ms: 1.03x faster                                             |
| pickle_dict          | 29.5 us                                                      | 30.4 us: 1.03x slower                                            |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.08x faster                                            |
| python_startup_no_site | 7.32 ms                                                      | 7.70 ms: 1.05x slower                                            |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                            |
| django_template | 52.0 ms                                                      | 39.5 ms: 1.32x faster                                            |
| genshi_text     | 31.7 ms                                                      | 24.4 ms: 1.30x faster                                            |
| genshi_xml      | 63.5 ms                                                      | 56.0 ms: 1.13x faster                                            |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-pythonperf2-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.98 ms: 1.90x faster                                            |
| go                      | 264 ms                                                       | 154 ms: 1.71x faster                                             |
| pyflate                 | 731 ms                                                       | 431 ms: 1.70x faster                                             |
| logging_silent          | 165 ns                                                       | 98.9 ns: 1.66x faster                                            |
| scimark_sor             | 177 ms                                                       | 108 ms: 1.65x faster                                             |
| raytrace                | 491 ms                                                       | 305 ms: 1.61x faster                                             |
| scimark_monte_carlo     | 109 ms                                                       | 67.5 ms: 1.61x faster                                            |
| bench_mp_pool           | 7.10 ms                                                      | 4.55 ms: 1.56x faster                                            |
| richards                | 73.9 ms                                                      | 48.5 ms: 1.52x faster                                            |
| chaos                   | 108 ms                                                       | 72.1 ms: 1.50x faster                                            |
| float                   | 109 ms                                                       | 73.8 ms: 1.48x faster                                            |
| spectral_norm           | 138 ms                                                       | 93.4 ms: 1.48x faster                                            |
| scimark_lu              | 164 ms                                                       | 111 ms: 1.47x faster                                             |
| crypto_pyaes            | 119 ms                                                       | 83.5 ms: 1.42x faster                                            |
| pickle_pure_python      | 451 us                                                       | 320 us: 1.41x faster                                             |
| xml_etree_process       | 77.6 ms                                                      | 55.8 ms: 1.39x faster                                            |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                           |
| async_tree_none         | 698 ms                                                       | 511 ms: 1.37x faster                                             |
| html5lib                | 96.3 ms                                                      | 70.5 ms: 1.37x faster                                            |
| hexiom                  | 9.54 ms                                                      | 6.99 ms: 1.36x faster                                            |
| nbody                   | 132 ms                                                       | 96.9 ms: 1.36x faster                                            |
| unpickle_pure_python    | 318 us                                                       | 234 us: 1.36x faster                                             |
| pprint_pformat          | 2.12 sec                                                     | 1.57 sec: 1.35x faster                                           |
| pprint_safe_repr        | 1.03 sec                                                     | 759 ms: 1.35x faster                                             |
| async_tree_memoization  | 822 ms                                                       | 609 ms: 1.35x faster                                             |
| mako                    | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                            |
| async_generators        | 419 ms                                                       | 313 ms: 1.34x faster                                             |
| deepcopy_memo           | 49.2 us                                                      | 36.9 us: 1.33x faster                                            |
| unpack_sequence         | 59.7 ns                                                      | 45.1 ns: 1.32x faster                                            |
| django_template         | 52.0 ms                                                      | 39.5 ms: 1.32x faster                                            |
| thrift                  | 1.23 ms                                                      | 935 us: 1.31x faster                                             |
| genshi_text             | 31.7 ms                                                      | 24.4 ms: 1.30x faster                                            |
| async_tree_cpu_io_mixed | 951 ms                                                       | 740 ms: 1.28x faster                                             |
| tornado_http            | 151 ms                                                       | 117 ms: 1.28x faster                                             |
| logging_simple          | 9.24 us                                                      | 7.21 us: 1.28x faster                                            |
| chameleon               | 9.62 ms                                                      | 7.52 ms: 1.28x faster                                            |
| pycparser               | 1.66 sec                                                     | 1.30 sec: 1.27x faster                                           |
| logging_format          | 9.94 us                                                      | 7.81 us: 1.27x faster                                            |
| scimark_fft             | 359 ms                                                       | 284 ms: 1.27x faster                                             |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.05 ms: 1.26x faster                                            |
| 2to3                    | 352 ms                                                       | 282 ms: 1.25x faster                                             |
| aiohttp                 | 1.18 ms                                                      | 944 us: 1.25x faster                                             |
| gunicorn                | 1.15 ms                                                      | 929 us: 1.23x faster                                             |
| sqlalchemy_declarative  | 188 ms                                                       | 153 ms: 1.23x faster                                             |
| regex_compile           | 191 ms                                                       | 157 ms: 1.22x faster                                             |
| docutils                | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                           |
| json_loads              | 30.3 us                                                      | 25.1 us: 1.21x faster                                            |
| dulwich_log             | 80.5 ms                                                      | 67.2 ms: 1.20x faster                                            |
| xml_etree_generate      | 94.1 ms                                                      | 79.0 ms: 1.19x faster                                            |
| sqlglot_normalize       | 147 ms                                                       | 124 ms: 1.19x faster                                             |
| deepcopy                | 457 us                                                       | 385 us: 1.19x faster                                             |
| sqlalchemy_imperative   | 22.9 ms                                                      | 19.4 ms: 1.18x faster                                            |
| sqlglot_transpile       | 2.69 ms                                                      | 2.29 ms: 1.17x faster                                            |
| sqlglot_optimize        | 70.1 ms                                                      | 59.7 ms: 1.17x faster                                            |
| dask                    | 478 ms                                                       | 410 ms: 1.17x faster                                             |
| sqlite_synth            | 2.96 us                                                      | 2.54 us: 1.16x faster                                            |
| nqueens                 | 114 ms                                                       | 97.7 ms: 1.16x faster                                            |
| sqlglot_parse           | 2.24 ms                                                      | 1.95 ms: 1.15x faster                                            |
| json                    | 5.94 ms                                                      | 5.16 ms: 1.15x faster                                            |
| regex_dna               | 261 ms                                                       | 227 ms: 1.15x faster                                             |
| bench_thread_pool       | 1.14 ms                                                      | 1.00 ms: 1.14x faster                                            |
| genshi_xml              | 63.5 ms                                                      | 56.0 ms: 1.13x faster                                            |
| sympy_expand            | 603 ms                                                       | 533 ms: 1.13x faster                                             |
| deepcopy_reduce         | 3.91 us                                                      | 3.47 us: 1.13x faster                                            |
| sympy_integrate         | 28.1 ms                                                      | 25.0 ms: 1.12x faster                                            |
| pathlib                 | 21.3 ms                                                      | 19.1 ms: 1.11x faster                                            |
| fannkuch                | 496 ms                                                       | 447 ms: 1.11x faster                                             |
| pylint                  | 562 ms                                                       | 510 ms: 1.10x faster                                             |
| create_gc_cycles        | 1.80 ms                                                      | 1.64 ms: 1.10x faster                                            |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                             |
| sympy_str               | 358 ms                                                       | 327 ms: 1.10x faster                                             |
| coroutines              | 30.6 ms                                                      | 27.9 ms: 1.10x faster                                            |
| sympy_sum               | 193 ms                                                       | 177 ms: 1.09x faster                                             |
| regex_v8                | 26.0 ms                                                      | 24.1 ms: 1.08x faster                                            |
| python_startup          | 11.5 ms                                                      | 10.7 ms: 1.08x faster                                            |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                             |
| json_dumps              | 14.3 ms                                                      | 13.3 ms: 1.07x faster                                            |
| pickle_list             | 4.11 us                                                      | 3.86 us: 1.07x faster                                            |
| mypy2                   | 466 ms                                                       | 439 ms: 1.06x faster                                             |
| asyncio_tcp             | 787 ms                                                       | 746 ms: 1.05x faster                                             |
| xml_etree_parse         | 160 ms                                                       | 153 ms: 1.04x faster                                             |
| pickle                  | 10.1 us                                                      | 9.77 us: 1.04x faster                                            |
| mdp                     | 2.95 sec                                                     | 2.85 sec: 1.04x faster                                           |
| unpickle_list           | 4.73 us                                                      | 4.57 us: 1.03x faster                                            |
| generators              | 57.0 ms                                                      | 55.2 ms: 1.03x faster                                            |
| xml_etree_iterparse     | 109 ms                                                       | 106 ms: 1.03x faster                                             |
| telco                   | 7.14 ms                                                      | 6.99 ms: 1.02x faster                                            |
| comprehensions          | 27.3 us                                                      | 27.9 us: 1.02x slower                                            |
| pickle_dict             | 29.5 us                                                      | 30.4 us: 1.03x slower                                            |
| regex_effbot            | 2.99 ms                                                      | 3.11 ms: 1.04x slower                                            |
| python_startup_no_site  | 7.32 ms                                                      | 7.70 ms: 1.05x slower                                            |
| gc_traversal            | 3.46 ms                                                      | 3.94 ms: 1.14x slower                                            |
| Geometric mean          | (ref)                                                        | 1.23x faster                                                     |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage, flaskblogging
