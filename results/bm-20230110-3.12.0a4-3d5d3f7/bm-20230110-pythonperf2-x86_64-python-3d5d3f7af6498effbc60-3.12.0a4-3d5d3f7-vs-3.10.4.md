
# Results vs. 3.10.4

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: linux-x86_64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 286 ms: 1.23x faster                                                        |
| chameleon      | 9.62 ms                                                      | 7.31 ms: 1.32x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                      |
| html5lib       | 96.3 ms                                                      | 66.8 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 72.4 ms: 1.51x faster                                                       |
| nbody          | 132 ms                                                       | 98.1 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 149 ms: 1.28x faster                                                        |
| regex_dna      | 261 ms                                                       | 229 ms: 1.14x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 23.0 ms: 1.13x faster                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 214 us: 1.48x faster                                                        |
| pickle_pure_python   | 451 us                                                       | 313 us: 1.44x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 10.1 ms: 1.41x faster                                                       |
| xml_etree_process    | 77.6 ms                                                      | 55.4 ms: 1.40x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.0 us: 1.26x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 80.3 ms: 1.17x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.70 us: 1.11x faster                                                       |
| unpickle_list        | 4.73 us                                                      | 4.48 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.04x faster                                                        |
| pickle               | 10.1 us                                                      | 9.71 us: 1.04x faster                                                       |
| pickle_dict          | 29.5 us                                                      | 31.1 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.87 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                       |
| django_template | 52.0 ms                                                      | 39.2 ms: 1.33x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 24.8 ms: 1.28x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 53.7 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.69 ms: 2.05x faster                                                       |
| asyncio_tcp             | 787 ms                                                       | 386 ms: 2.04x faster                                                        |
| go                      | 264 ms                                                       | 153 ms: 1.72x faster                                                        |
| pyflate                 | 731 ms                                                       | 433 ms: 1.69x faster                                                        |
| raytrace                | 491 ms                                                       | 299 ms: 1.64x faster                                                        |
| scimark_sor             | 177 ms                                                       | 108 ms: 1.64x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 66.6 ms: 1.63x faster                                                       |
| scimark_lu              | 164 ms                                                       | 101 ms: 1.63x faster                                                        |
| logging_silent          | 165 ns                                                       | 102 ns: 1.62x faster                                                        |
| richards                | 73.9 ms                                                      | 46.9 ms: 1.58x faster                                                       |
| chaos                   | 108 ms                                                       | 70.9 ms: 1.52x faster                                                       |
| float                   | 109 ms                                                       | 72.4 ms: 1.51x faster                                                       |
| unpickle_pure_python    | 318 us                                                       | 214 us: 1.48x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 81.1 ms: 1.46x faster                                                       |
| pickle_pure_python      | 451 us                                                       | 313 us: 1.44x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                       |
| html5lib                | 96.3 ms                                                      | 66.8 ms: 1.44x faster                                                       |
| bench_mp_pool           | 7.10 ms                                                      | 4.94 ms: 1.44x faster                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 1.59 ms: 1.41x faster                                                       |
| json_dumps              | 14.3 ms                                                      | 10.1 ms: 1.41x faster                                                       |
| hexiom                  | 9.54 ms                                                      | 6.77 ms: 1.41x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 55.4 ms: 1.40x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.15 sec: 1.40x faster                                                      |
| async_tree_none         | 698 ms                                                       | 505 ms: 1.38x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.95 ms: 1.38x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.70 ms: 1.38x faster                                                       |
| spectral_norm           | 138 ms                                                       | 101 ms: 1.36x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 44.0 ns: 1.36x faster                                                       |
| async_tree_memoization  | 822 ms                                                       | 608 ms: 1.35x faster                                                        |
| thrift                  | 1.23 ms                                                      | 908 us: 1.35x faster                                                        |
| nbody                   | 132 ms                                                       | 98.1 ms: 1.35x faster                                                       |
| deepcopy_memo           | 49.2 us                                                      | 36.7 us: 1.34x faster                                                       |
| logging_simple          | 9.24 us                                                      | 6.95 us: 1.33x faster                                                       |
| django_template         | 52.0 ms                                                      | 39.2 ms: 1.33x faster                                                       |
| chameleon               | 9.62 ms                                                      | 7.31 ms: 1.32x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                      |
| pprint_pformat          | 2.12 sec                                                     | 1.63 sec: 1.31x faster                                                      |
| fannkuch                | 496 ms                                                       | 380 ms: 1.31x faster                                                        |
| async_generators        | 419 ms                                                       | 322 ms: 1.30x faster                                                        |
| logging_format          | 9.94 us                                                      | 7.66 us: 1.30x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 794 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 742 ms: 1.28x faster                                                        |
| regex_compile           | 191 ms                                                       | 149 ms: 1.28x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 24.8 ms: 1.28x faster                                                       |
| scimark_fft             | 359 ms                                                       | 283 ms: 1.27x faster                                                        |
| json_loads              | 30.3 us                                                      | 24.0 us: 1.26x faster                                                       |
| 2to3                    | 352 ms                                                       | 286 ms: 1.23x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                      |
| mypy2                   | 466 ms                                                       | 380 ms: 1.23x faster                                                        |
| nqueens                 | 114 ms                                                       | 94.0 ms: 1.21x faster                                                       |
| deepcopy                | 457 us                                                       | 379 us: 1.21x faster                                                        |
| sqlglot_normalize       | 147 ms                                                       | 123 ms: 1.20x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 67.5 ms: 1.19x faster                                                       |
| genshi_xml              | 63.5 ms                                                      | 53.7 ms: 1.18x faster                                                       |
| sqlglot_optimize        | 70.1 ms                                                      | 59.3 ms: 1.18x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.33 us: 1.17x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 80.3 ms: 1.17x faster                                                       |
| dask                    | 478 ms                                                       | 408 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.56 us: 1.16x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 987 us: 1.15x faster                                                        |
| regex_dna               | 261 ms                                                       | 229 ms: 1.14x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.58 ms: 1.14x faster                                                       |
| json                    | 5.94 ms                                                      | 5.24 ms: 1.13x faster                                                       |
| regex_v8                | 26.0 ms                                                      | 23.0 ms: 1.13x faster                                                       |
| sympy_expand            | 603 ms                                                       | 537 ms: 1.12x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.70 us: 1.11x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.6 ms: 1.10x faster                                                       |
| coroutines              | 30.6 ms                                                      | 27.9 ms: 1.10x faster                                                       |
| pathlib                 | 21.3 ms                                                      | 19.4 ms: 1.10x faster                                                       |
| meteor_contest          | 142 ms                                                       | 131 ms: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.75 sec: 1.07x faster                                                      |
| sympy_str               | 358 ms                                                       | 335 ms: 1.07x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.70 ms: 1.07x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| unpickle_list           | 4.73 us                                                      | 4.48 us: 1.05x faster                                                       |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.04x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.71 us: 1.04x faster                                                       |
| sympy_sum               | 193 ms                                                       | 186 ms: 1.04x faster                                                        |
| comprehensions          | 27.3 us                                                      | 27.1 us: 1.01x faster                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.54 ms: 1.02x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 31.1 us: 1.05x slower                                                       |
| generators              | 57.0 ms                                                      | 60.5 ms: 1.06x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.87 ms: 1.07x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                                       |
| coverage                | 71.1 ms                                                      | 89.3 ms: 1.26x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
