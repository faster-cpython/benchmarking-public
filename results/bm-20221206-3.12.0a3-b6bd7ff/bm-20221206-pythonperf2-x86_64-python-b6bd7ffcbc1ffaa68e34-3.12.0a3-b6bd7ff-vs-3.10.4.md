
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 281 ms: 1.25x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.51 ms: 1.28x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.76 sec: 1.24x faster                                                      |
| html5lib       | 96.3 ms                                                      | 66.2 ms: 1.45x faster                                                       |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 73.2 ms: 1.50x faster                                                       |
| nbody          | 132 ms                                                       | 94.3 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 150 ms: 1.27x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 22.3 ms: 1.17x faster                                                       |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 212 us: 1.50x faster                                                        |
| pickle_pure_python   | 451 us                                                       | 316 us: 1.43x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 55.6 ms: 1.39x faster                                                       |
| json_dumps           | 14.3 ms                                                      | 10.3 ms: 1.38x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 78.9 ms: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| unpickle_list        | 4.73 us                                                      | 4.47 us: 1.06x faster                                                       |
| pickle_list          | 4.11 us                                                      | 3.90 us: 1.06x faster                                                       |
| pickle               | 10.1 us                                                      | 9.84 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 108 ms: 1.01x faster                                                        |
| unpickle             | 13.3 us                                                      | 13.1 us: 1.01x faster                                                       |
| pickle_dict          | 29.5 us                                                      | 31.9 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.86 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| django_template | 52.0 ms                                                      | 39.6 ms: 1.31x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 25.8 ms: 1.23x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 53.5 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.67 ms: 2.06x faster                                                       |
| pyflate                 | 731 ms                                                       | 440 ms: 1.66x faster                                                        |
| go                      | 264 ms                                                       | 159 ms: 1.66x faster                                                        |
| logging_silent          | 165 ns                                                       | 99.7 ns: 1.65x faster                                                       |
| scimark_lu              | 164 ms                                                       | 100 ms: 1.64x faster                                                        |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.62x faster                                                        |
| richards                | 73.9 ms                                                      | 46.1 ms: 1.60x faster                                                       |
| bench_mp_pool           | 7.10 ms                                                      | 4.46 ms: 1.59x faster                                                       |
| raytrace                | 491 ms                                                       | 327 ms: 1.50x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 212 us: 1.50x faster                                                        |
| float                   | 109 ms                                                       | 73.2 ms: 1.50x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 72.7 ms: 1.49x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 1.52 ms: 1.48x faster                                                       |
| html5lib                | 96.3 ms                                                      | 66.2 ms: 1.45x faster                                                       |
| crypto_pyaes            | 119 ms                                                       | 81.8 ms: 1.45x faster                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 1.87 ms: 1.43x faster                                                       |
| spectral_norm           | 138 ms                                                       | 96.2 ms: 1.43x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 316 us: 1.43x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.73 ms: 1.42x faster                                                       |
| nbody                   | 132 ms                                                       | 94.3 ms: 1.40x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 55.6 ms: 1.39x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 10.3 ms: 1.38x faster                                                       |
| chaos                   | 108 ms                                                       | 78.3 ms: 1.38x faster                                                       |
| thrift                  | 1.23 ms                                                      | 894 us: 1.37x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.18 sec: 1.37x faster                                                      |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.73 ms: 1.36x faster                                                       |
| pprint_pformat          | 2.12 sec                                                     | 1.56 sec: 1.36x faster                                                      |
| deepcopy_memo           | 49.2 us                                                      | 36.2 us: 1.36x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 758 ms: 1.35x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 623 ms: 1.32x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                      |
| async_tree_none         | 698 ms                                                       | 531 ms: 1.31x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 45.5 ns: 1.31x faster                                                       |
| django_template         | 52.0 ms                                                      | 39.6 ms: 1.31x faster                                                       |
| logging_simple          | 9.24 us                                                      | 7.03 us: 1.31x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.72 us: 1.29x faster                                                       |
| chameleon               | 9.62 ms                                                      | 7.51 ms: 1.28x faster                                                       |
| regex_compile           | 191 ms                                                       | 150 ms: 1.27x faster                                                        |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.27x faster                                                        |
| 2to3                    | 352 ms                                                       | 281 ms: 1.25x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.2 us: 1.25x faster                                                       |
| async_generators        | 419 ms                                                       | 335 ms: 1.25x faster                                                        |
| fannkuch                | 496 ms                                                       | 398 ms: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 375 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 767 ms: 1.24x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.76 sec: 1.24x faster                                                      |
| genshi_text             | 31.7 ms                                                      | 25.8 ms: 1.23x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 121 ms: 1.21x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 66.7 ms: 1.21x faster                                                       |
| deepcopy                | 457 us                                                       | 380 us: 1.20x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.5 ms: 1.20x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 78.9 ms: 1.19x faster                                                       |
| genshi_xml              | 63.5 ms                                                      | 53.5 ms: 1.19x faster                                                       |
| dask                    | 478 ms                                                       | 409 ms: 1.17x faster                                                        |
| regex_v8                | 26.0 ms                                                      | 22.3 ms: 1.17x faster                                                       |
| json                    | 5.94 ms                                                      | 5.11 ms: 1.16x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.37 us: 1.16x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 994 us: 1.15x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.60 us: 1.14x faster                                                       |
| xml_etree_parse         | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.60 ms: 1.13x faster                                                       |
| sympy_expand            | 603 ms                                                       | 539 ms: 1.12x faster                                                        |
| regex_dna               | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 19.0 ms: 1.12x faster                                                       |
| nqueens                 | 114 ms                                                       | 102 ms: 1.11x faster                                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.6 ms: 1.10x faster                                                       |
| coroutines              | 30.6 ms                                                      | 28.0 ms: 1.09x faster                                                       |
| pidigits                | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.60 ms: 1.08x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.73 sec: 1.08x faster                                                      |
| sympy_str               | 358 ms                                                       | 331 ms: 1.08x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 743 ms: 1.06x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.47 us: 1.06x faster                                                       |
| pickle_list             | 4.11 us                                                      | 3.90 us: 1.06x faster                                                       |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.84 us: 1.03x faster                                                       |
| xml_etree_iterparse     | 109 ms                                                       | 108 ms: 1.01x faster                                                        |
| unpickle                | 13.3 us                                                      | 13.1 us: 1.01x faster                                                       |
| generators              | 57.0 ms                                                      | 60.8 ms: 1.07x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.86 ms: 1.07x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 31.9 us: 1.08x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.79 ms: 1.10x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                                       |
| coverage                | 71.1 ms                                                      | 85.0 ms: 1.20x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                                |

Benchmark hidden because not significant (1): comprehensions
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
