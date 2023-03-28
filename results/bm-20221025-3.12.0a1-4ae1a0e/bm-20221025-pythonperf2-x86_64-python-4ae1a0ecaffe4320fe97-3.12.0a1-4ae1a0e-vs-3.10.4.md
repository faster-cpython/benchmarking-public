
# Results vs. 3.10.4

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: linux-x86_64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 278 ms: 1.27x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.62 ms: 1.26x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| html5lib       | 96.3 ms                                                      | 66.2 ms: 1.45x faster                                                       |
| tornado_http   | 151 ms                                                       | 114 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.2 ms: 1.50x faster                                                       |
| nbody          | 132 ms                                                       | 98.1 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 146 ms: 1.31x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 22.9 ms: 1.14x faster                                                       |
| regex_dna      | 261 ms                                                       | 232 ms: 1.12x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.34 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 208 us: 1.53x faster                                                        |
| pickle_pure_python   | 451 us                                                       | 313 us: 1.44x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 54.1 ms: 1.43x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 10.4 ms: 1.38x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.3 us: 1.25x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 77.6 ms: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.84 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.47 us: 1.06x faster                                                       |
| pickle_dict          | 29.5 us                                                      | 31.9 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.6 ms: 1.08x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.62 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 24.7 ms: 1.28x faster                                                       |
| django_template | 52.0 ms                                                      | 40.6 ms: 1.28x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 55.5 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-pythonperf2-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.65 ms: 2.06x faster                                                       |
| logging_silent          | 165 ns                                                       | 95.5 ns: 1.72x faster                                                       |
| go                      | 264 ms                                                       | 155 ms: 1.71x faster                                                        |
| pyflate                 | 731 ms                                                       | 431 ms: 1.70x faster                                                        |
| raytrace                | 491 ms                                                       | 298 ms: 1.65x faster                                                        |
| scimark_sor             | 177 ms                                                       | 108 ms: 1.63x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 67.8 ms: 1.60x faster                                                       |
| bench_mp_pool           | 7.10 ms                                                      | 4.56 ms: 1.56x faster                                                       |
| richards                | 73.9 ms                                                      | 47.6 ms: 1.55x faster                                                       |
| unpickle_pure_python    | 318 us                                                       | 208 us: 1.53x faster                                                        |
| float                   | 109 ms                                                       | 73.2 ms: 1.50x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 1.51 ms: 1.48x faster                                                       |
| scimark_lu              | 164 ms                                                       | 111 ms: 1.48x faster                                                        |
| chaos                   | 108 ms                                                       | 73.4 ms: 1.47x faster                                                       |
| html5lib                | 96.3 ms                                                      | 66.2 ms: 1.45x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.61 ms: 1.44x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 313 us: 1.44x faster                                                        |
| spectral_norm           | 138 ms                                                       | 96.1 ms: 1.43x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 54.1 ms: 1.43x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 83.2 ms: 1.42x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.58 ms: 1.42x faster                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 1.90 ms: 1.42x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                      |
| json_dumps              | 14.3 ms                                                      | 10.4 ms: 1.38x faster                                                       |
| pprint_pformat          | 2.12 sec                                                     | 1.57 sec: 1.36x faster                                                      |
| deepcopy_memo           | 49.2 us                                                      | 36.4 us: 1.35x faster                                                       |
| async_tree_none         | 698 ms                                                       | 516 ms: 1.35x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 761 ms: 1.35x faster                                                        |
| nbody                   | 132 ms                                                       | 98.1 ms: 1.35x faster                                                       |
| async_tree_memoization  | 822 ms                                                       | 618 ms: 1.33x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 45.0 ns: 1.33x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.25 sec: 1.32x faster                                                      |
| tornado_http            | 151 ms                                                       | 114 ms: 1.32x faster                                                        |
| aiohttp                 | 1.18 ms                                                      | 894 us: 1.32x faster                                                        |
| regex_compile           | 191 ms                                                       | 146 ms: 1.31x faster                                                        |
| logging_simple          | 9.24 us                                                      | 7.06 us: 1.31x faster                                                       |
| async_generators        | 419 ms                                                       | 321 ms: 1.30x faster                                                        |
| gunicorn                | 1.15 ms                                                      | 888 us: 1.29x faster                                                        |
| thrift                  | 1.23 ms                                                      | 953 us: 1.29x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 24.7 ms: 1.28x faster                                                       |
| django_template         | 52.0 ms                                                      | 40.6 ms: 1.28x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.77 us: 1.28x faster                                                       |
| 2to3                    | 352 ms                                                       | 278 ms: 1.27x faster                                                        |
| chameleon               | 9.62 ms                                                      | 7.62 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 756 ms: 1.26x faster                                                        |
| mypy2                   | 466 ms                                                       | 372 ms: 1.25x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.3 us: 1.25x faster                                                       |
| scimark_fft             | 359 ms                                                       | 288 ms: 1.25x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.23x faster                                                        |
| fannkuch                | 496 ms                                                       | 405 ms: 1.23x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 65.9 ms: 1.22x faster                                                       |
| docutils                | 3.41 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| xml_etree_generate      | 94.1 ms                                                      | 77.6 ms: 1.21x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 58.2 ms: 1.20x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 966 us: 1.18x faster                                                        |
| json                    | 5.94 ms                                                      | 5.05 ms: 1.18x faster                                                       |
| nqueens                 | 114 ms                                                       | 97.1 ms: 1.17x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.35 us: 1.17x faster                                                       |
| dask                    | 478 ms                                                       | 409 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.54 us: 1.16x faster                                                       |
| deepcopy                | 457 us                                                       | 394 us: 1.16x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 55.5 ms: 1.15x faster                                                       |
| sympy_expand            | 603 ms                                                       | 527 ms: 1.14x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 22.9 ms: 1.14x faster                                                       |
| pylint                  | 562 ms                                                       | 496 ms: 1.13x faster                                                        |
| meteor_contest          | 142 ms                                                       | 126 ms: 1.13x faster                                                        |
| comprehensions          | 27.3 us                                                      | 24.2 us: 1.13x faster                                                       |
| regex_dna               | 261 ms                                                       | 232 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.61 ms: 1.12x faster                                                       |
| pathlib                 | 21.3 ms                                                      | 19.0 ms: 1.12x faster                                                       |
| coroutines              | 30.6 ms                                                      | 27.4 ms: 1.11x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.4 ms: 1.11x faster                                                       |
| sympy_str               | 358 ms                                                       | 326 ms: 1.10x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.71 sec: 1.09x faster                                                      |
| python_startup          | 11.5 ms                                                      | 10.6 ms: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.64 ms: 1.08x faster                                                       |
| pickle_list             | 4.11 us                                                      | 3.84 us: 1.07x faster                                                       |
| sympy_sum               | 193 ms                                                       | 181 ms: 1.06x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 103 ms: 1.06x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.47 us: 1.06x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 747 ms: 1.05x faster                                                        |
| generators              | 57.0 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.54 ms: 1.02x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.62 ms: 1.04x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 31.9 us: 1.08x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.34 ms: 1.12x slower                                                       |
| coverage                | 71.1 ms                                                      | 81.5 ms: 1.15x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                |

Benchmark hidden because not significant (2): pickle, unpickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
