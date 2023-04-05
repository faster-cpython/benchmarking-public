
# Results vs. 3.10.4

- fork: python
- ref: b1b375e2670a58fc37cb
- machine: linux-x86_64
- commit hash: b1b375e
- commit date: 2023-02-19
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 279 ms: 1.26x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.14 ms: 1.35x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.80 sec: 1.22x faster                                                       |
| html5lib       | 96.3 ms                                                      | 68.0 ms: 1.42x faster                                                        |
| tornado_http   | 151 ms                                                       | 117 ms: 1.29x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 70.9 ms: 1.54x faster                                                        |
| nbody          | 132 ms                                                       | 90.4 ms: 1.46x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 142 ms: 1.34x faster                                                         |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 22.9 ms: 1.13x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.42 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 206 us: 1.54x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 305 us: 1.48x faster                                                         |
| json_dumps           | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                        |
| xml_etree_process    | 77.6 ms                                                      | 57.1 ms: 1.36x faster                                                        |
| json_loads           | 30.3 us                                                      | 23.9 us: 1.27x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| xml_etree_generate   | 94.1 ms                                                      | 83.2 ms: 1.13x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.79 us: 1.08x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 101 ms: 1.08x faster                                                         |
| unpickle_list        | 4.73 us                                                      | 4.44 us: 1.06x faster                                                        |
| pickle               | 10.1 us                                                      | 10.3 us: 1.01x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 32.3 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.28 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.92 ms: 1.49x faster                                                        |
| django_template | 52.0 ms                                                      | 38.3 ms: 1.36x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 24.7 ms: 1.28x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 53.6 ms: 1.19x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-pythonperf2-x86_64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.32 ms: 2.27x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 386 ms: 2.04x faster                                                         |
| logging_silent          | 165 ns                                                       | 92.7 ns: 1.77x faster                                                        |
| go                      | 264 ms                                                       | 150 ms: 1.76x faster                                                         |
| pyflate                 | 731 ms                                                       | 434 ms: 1.69x faster                                                         |
| scimark_sor             | 177 ms                                                       | 105 ms: 1.68x faster                                                         |
| raytrace                | 491 ms                                                       | 293 ms: 1.68x faster                                                         |
| richards                | 73.9 ms                                                      | 44.8 ms: 1.65x faster                                                        |
| scimark_lu              | 164 ms                                                       | 99.6 ms: 1.65x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 66.8 ms: 1.63x faster                                                        |
| float                   | 109 ms                                                       | 70.9 ms: 1.54x faster                                                        |
| unpickle_pure_python    | 318 us                                                       | 206 us: 1.54x faster                                                         |
| chaos                   | 108 ms                                                       | 71.8 ms: 1.50x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 6.39 ms: 1.49x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.77 ms: 1.49x faster                                                        |
| mako                    | 14.7 ms                                                      | 9.92 ms: 1.49x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 305 us: 1.48x faster                                                         |
| crypto_pyaes            | 119 ms                                                       | 80.4 ms: 1.47x faster                                                        |
| nbody                   | 132 ms                                                       | 90.4 ms: 1.46x faster                                                        |
| spectral_norm           | 138 ms                                                       | 94.6 ms: 1.46x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.55 ms: 1.45x faster                                                        |
| generators              | 57.0 ms                                                      | 39.9 ms: 1.43x faster                                                        |
| html5lib                | 96.3 ms                                                      | 68.0 ms: 1.42x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 35.0 us: 1.41x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.92 ms: 1.40x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.2 ms: 1.40x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                       |
| async_tree_none         | 698 ms                                                       | 507 ms: 1.38x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.21 sec: 1.37x faster                                                       |
| pprint_pformat          | 2.12 sec                                                     | 1.55 sec: 1.37x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 57.1 ms: 1.36x faster                                                        |
| django_template         | 52.0 ms                                                      | 38.3 ms: 1.36x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 759 ms: 1.35x faster                                                         |
| chameleon               | 9.62 ms                                                      | 7.14 ms: 1.35x faster                                                        |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.78 ms: 1.35x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 44.4 ns: 1.34x faster                                                        |
| async_tree_memoization  | 822 ms                                                       | 613 ms: 1.34x faster                                                         |
| regex_compile           | 191 ms                                                       | 142 ms: 1.34x faster                                                         |
| thrift                  | 1.23 ms                                                      | 915 us: 1.34x faster                                                         |
| logging_simple          | 9.24 us                                                      | 6.94 us: 1.33x faster                                                        |
| tornado_http            | 151 ms                                                       | 117 ms: 1.29x faster                                                         |
| comprehensions          | 27.3 us                                                      | 21.1 us: 1.29x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 24.7 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 744 ms: 1.28x faster                                                         |
| coroutines              | 30.6 ms                                                      | 24.0 ms: 1.27x faster                                                        |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.27x faster                                                         |
| logging_format          | 9.94 us                                                      | 7.82 us: 1.27x faster                                                        |
| json_loads              | 30.3 us                                                      | 23.9 us: 1.27x faster                                                        |
| mypy2                   | 466 ms                                                       | 368 ms: 1.27x faster                                                         |
| 2to3                    | 352 ms                                                       | 279 ms: 1.26x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 65.2 ms: 1.24x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 120 ms: 1.23x faster                                                         |
| docutils                | 3.41 sec                                                     | 2.80 sec: 1.22x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 57.6 ms: 1.22x faster                                                        |
| deepcopy                | 457 us                                                       | 384 us: 1.19x faster                                                         |
| bench_thread_pool       | 1.14 ms                                                      | 956 us: 1.19x faster                                                         |
| json                    | 5.94 ms                                                      | 5.00 ms: 1.19x faster                                                        |
| genshi_xml              | 63.5 ms                                                      | 53.6 ms: 1.19x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.34 us: 1.17x faster                                                        |
| nqueens                 | 114 ms                                                       | 96.9 ms: 1.17x faster                                                        |
| fannkuch                | 496 ms                                                       | 426 ms: 1.17x faster                                                         |
| regex_dna               | 261 ms                                                       | 225 ms: 1.16x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 24.5 ms: 1.15x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 141 ms: 1.14x faster                                                         |
| sympy_str               | 358 ms                                                       | 315 ms: 1.14x faster                                                         |
| regex_v8                | 26.0 ms                                                      | 22.9 ms: 1.13x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 83.2 ms: 1.13x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.63 us: 1.13x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.62 sec: 1.13x faster                                                       |
| sympy_expand            | 603 ms                                                       | 535 ms: 1.13x faster                                                         |
| async_generators        | 419 ms                                                       | 375 ms: 1.12x faster                                                         |
| create_gc_cycles        | 1.80 ms                                                      | 1.62 ms: 1.11x faster                                                        |
| meteor_contest          | 142 ms                                                       | 128 ms: 1.11x faster                                                         |
| pathlib                 | 21.3 ms                                                      | 19.4 ms: 1.10x faster                                                        |
| sympy_sum               | 193 ms                                                       | 176 ms: 1.10x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.79 us: 1.08x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 101 ms: 1.08x faster                                                         |
| pidigits                | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| unpickle_list           | 4.73 us                                                      | 4.44 us: 1.06x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.73 ms: 1.06x faster                                                        |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.02x faster                                                        |
| pickle                  | 10.1 us                                                      | 10.3 us: 1.01x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.57 ms: 1.03x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 32.3 us: 1.09x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.28 ms: 1.13x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.42 ms: 1.14x slower                                                        |
| dask                    | 478 ms                                                       | 558 ms: 1.17x slower                                                         |
| coverage                | 71.1 ms                                                      | 85.0 ms: 1.20x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
