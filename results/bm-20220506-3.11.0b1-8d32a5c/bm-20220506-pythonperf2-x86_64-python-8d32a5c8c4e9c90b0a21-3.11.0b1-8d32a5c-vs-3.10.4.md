
# Results vs. 3.10.4

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 281 ms: 1.25x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.53 ms: 1.28x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                                      |
| html5lib       | 96.3 ms                                                      | 69.0 ms: 1.40x faster                                                       |
| tornado_http   | 151 ms                                                       | 121 ms: 1.24x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 74.7 ms: 1.46x faster                                                       |
| nbody          | 132 ms                                                       | 100 ms: 1.32x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 153 ms: 1.25x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 22.8 ms: 1.14x faster                                                       |
| regex_dna      | 261 ms                                                       | 232 ms: 1.13x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 2.97 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 451 us                                                       | 320 us: 1.41x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 56.1 ms: 1.38x faster                                                       |
| unpickle_pure_python | 318 us                                                       | 233 us: 1.37x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 80.3 ms: 1.17x faster                                                       |
| pickle_list          | 4.11 us                                                      | 3.81 us: 1.08x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 13.5 ms: 1.06x faster                                                       |
| pickle               | 10.1 us                                                      | 9.62 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 105 ms: 1.04x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.56 us: 1.04x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 155 ms: 1.03x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 29.9 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.5 ms: 1.09x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.68 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                       |
| django_template | 52.0 ms                                                      | 41.3 ms: 1.26x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 25.4 ms: 1.25x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 56.7 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf2-x86_64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.93 ms: 1.92x faster                                                       |
| pyflate                 | 731 ms                                                       | 433 ms: 1.69x faster                                                        |
| go                      | 264 ms                                                       | 156 ms: 1.69x faster                                                        |
| logging_silent          | 165 ns                                                       | 99.8 ns: 1.65x faster                                                       |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.61x faster                                                        |
| raytrace                | 491 ms                                                       | 309 ms: 1.59x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 69.2 ms: 1.57x faster                                                       |
| bench_mp_pool           | 7.10 ms                                                      | 4.56 ms: 1.56x faster                                                       |
| chaos                   | 108 ms                                                       | 72.4 ms: 1.49x faster                                                       |
| spectral_norm           | 138 ms                                                       | 93.1 ms: 1.48x faster                                                       |
| richards                | 73.9 ms                                                      | 50.1 ms: 1.47x faster                                                       |
| float                   | 109 ms                                                       | 74.7 ms: 1.46x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 82.3 ms: 1.44x faster                                                       |
| scimark_lu              | 164 ms                                                       | 114 ms: 1.44x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 320 us: 1.41x faster                                                        |
| html5lib                | 96.3 ms                                                      | 69.0 ms: 1.40x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 56.1 ms: 1.38x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                      |
| hexiom                  | 9.54 ms                                                      | 6.91 ms: 1.38x faster                                                       |
| unpickle_pure_python    | 318 us                                                       | 233 us: 1.37x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 755 ms: 1.36x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.57 sec: 1.36x faster                                                      |
| async_tree_none         | 698 ms                                                       | 516 ms: 1.35x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                       |
| thrift                  | 1.23 ms                                                      | 913 us: 1.34x faster                                                        |
| logging_simple          | 9.24 us                                                      | 6.90 us: 1.34x faster                                                       |
| nbody                   | 132 ms                                                       | 100 ms: 1.32x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 624 ms: 1.32x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                      |
| async_generators        | 419 ms                                                       | 318 ms: 1.32x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 37.6 us: 1.31x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.67 us: 1.30x faster                                                       |
| unpack_sequence         | 59.7 ns                                                      | 46.2 ns: 1.29x faster                                                       |
| chameleon               | 9.62 ms                                                      | 7.53 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 748 ms: 1.27x faster                                                        |
| django_template         | 52.0 ms                                                      | 41.3 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.06 ms: 1.25x faster                                                       |
| regex_compile           | 191 ms                                                       | 153 ms: 1.25x faster                                                        |
| 2to3                    | 352 ms                                                       | 281 ms: 1.25x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 25.4 ms: 1.25x faster                                                       |
| aiohttp                 | 1.18 ms                                                      | 945 us: 1.25x faster                                                        |
| tornado_http            | 151 ms                                                       | 121 ms: 1.24x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 119 ms: 1.24x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 928 us: 1.24x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.6 us: 1.23x faster                                                       |
| sqlalchemy_declarative  | 188 ms                                                       | 153 ms: 1.23x faster                                                        |
| scimark_fft             | 359 ms                                                       | 294 ms: 1.22x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.82 sec: 1.21x faster                                                      |
| sqlglot_optimize        | 70.1 ms                                                      | 58.9 ms: 1.19x faster                                                       |
| fannkuch                | 496 ms                                                       | 418 ms: 1.19x faster                                                        |
| nqueens                 | 114 ms                                                       | 95.8 ms: 1.19x faster                                                       |
| dulwich_log             | 80.5 ms                                                      | 68.0 ms: 1.18x faster                                                       |
| sqlite_synth            | 2.96 us                                                      | 2.51 us: 1.18x faster                                                       |
| sqlalchemy_imperative   | 22.9 ms                                                      | 19.5 ms: 1.17x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 80.3 ms: 1.17x faster                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 2.30 ms: 1.17x faster                                                       |
| deepcopy                | 457 us                                                       | 394 us: 1.16x faster                                                        |
| json                    | 5.94 ms                                                      | 5.14 ms: 1.15x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 1.95 ms: 1.15x faster                                                       |
| flaskblogging           | 4.37 ms                                                      | 3.82 ms: 1.15x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.42 us: 1.14x faster                                                       |
| regex_v8                | 26.0 ms                                                      | 22.8 ms: 1.14x faster                                                       |
| dask                    | 478 ms                                                       | 418 ms: 1.14x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 18.8 ms: 1.13x faster                                                       |
| regex_dna               | 261 ms                                                       | 232 ms: 1.13x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 56.7 ms: 1.12x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.02 ms: 1.12x faster                                                       |
| sympy_expand            | 603 ms                                                       | 540 ms: 1.12x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.2 ms: 1.12x faster                                                       |
| pylint                  | 562 ms                                                       | 505 ms: 1.11x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.64 ms: 1.10x faster                                                       |
| coroutines              | 30.6 ms                                                      | 28.0 ms: 1.09x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.5 ms: 1.09x faster                                                       |
| sympy_str               | 358 ms                                                       | 329 ms: 1.09x faster                                                        |
| sympy_sum               | 193 ms                                                       | 178 ms: 1.08x faster                                                        |
| meteor_contest          | 142 ms                                                       | 131 ms: 1.08x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.81 us: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| mypy2                   | 466 ms                                                       | 438 ms: 1.07x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.78 sec: 1.06x faster                                                      |
| json_dumps              | 14.3 ms                                                      | 13.5 ms: 1.06x faster                                                       |
| pickle                  | 10.1 us                                                      | 9.62 us: 1.05x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 749 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 105 ms: 1.04x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.56 us: 1.04x faster                                                       |
| xml_etree_parse         | 160 ms                                                       | 155 ms: 1.03x faster                                                        |
| generators              | 57.0 ms                                                      | 55.5 ms: 1.03x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.99 ms: 1.02x faster                                                       |
| regex_effbot            | 2.99 ms                                                      | 2.97 ms: 1.01x faster                                                       |
| pickle_dict             | 29.5 us                                                      | 29.9 us: 1.01x slower                                                       |
| comprehensions          | 27.3 us                                                      | 28.2 us: 1.03x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.68 ms: 1.05x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.85 ms: 1.11x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.23x faster                                                                |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage
