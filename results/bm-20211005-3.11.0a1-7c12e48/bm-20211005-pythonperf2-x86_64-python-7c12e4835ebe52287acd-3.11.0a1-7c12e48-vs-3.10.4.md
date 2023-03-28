
# Results vs. 3.10.4

- fork: python
- ref: 7c12e4835ebe52287acd
- machine: linux-x86_64
- commit hash: 7c12e48
- commit date: 2021-10-05
- overall geometric mean: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 329 ms: 1.07x faster                                                        |
| chameleon      | 9.62 ms                                                      | 8.97 ms: 1.07x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.22 sec: 1.06x faster                                                      |
| html5lib       | 96.3 ms                                                      | 83.0 ms: 1.16x faster                                                       |
| tornado_http   | 151 ms                                                       | 136 ms: 1.11x faster                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 86.6 ms: 1.26x faster                                                       |
| pidigits       | 271 ms                                                       | 266 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 169 ms: 1.13x faster                                                        |
| regex_v8       | 26.0 ms                                                      | 25.6 ms: 1.02x faster                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.05 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 77.6 ms                                                      | 64.1 ms: 1.21x faster                                                       |
| pickle_pure_python   | 451 us                                                       | 394 us: 1.15x faster                                                        |
| json_loads           | 30.3 us                                                      | 27.0 us: 1.12x faster                                                       |
| xml_etree_generate   | 94.1 ms                                                      | 86.0 ms: 1.09x faster                                                       |
| unpickle_pure_python | 318 us                                                       | 293 us: 1.09x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 13.6 ms: 1.05x faster                                                       |
| unpickle_list        | 4.73 us                                                      | 4.54 us: 1.04x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 158 ms: 1.01x faster                                                        |
| pickle_list          | 4.11 us                                                      | 4.14 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 109 ms                                                       | 111 ms: 1.02x slower                                                        |
| pickle               | 10.1 us                                                      | 10.4 us: 1.03x slower                                                       |
| unpickle             | 13.3 us                                                      | 13.7 us: 1.03x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 31.5 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.8 ms: 1.03x slower                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.57 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 13.1 ms: 1.13x faster                                                       |
| genshi_text     | 31.7 ms                                                      | 28.3 ms: 1.12x faster                                                       |
| django_template | 52.0 ms                                                      | 47.5 ms: 1.09x faster                                                       |
| genshi_xml      | 63.5 ms                                                      | 59.9 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| bench_mp_pool           | 7.10 ms                                                      | 5.14 ms: 1.38x faster                                                       |
| logging_simple          | 9.24 us                                                      | 6.69 us: 1.38x faster                                                       |
| logging_format          | 9.94 us                                                      | 7.28 us: 1.36x faster                                                       |
| async_tree_none         | 698 ms                                                       | 515 ms: 1.36x faster                                                        |
| raytrace                | 491 ms                                                       | 371 ms: 1.33x faster                                                        |
| deltablue               | 7.54 ms                                                      | 5.73 ms: 1.32x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.24 sec: 1.30x faster                                                      |
| unpack_sequence         | 59.7 ns                                                      | 46.5 ns: 1.28x faster                                                       |
| float                   | 109 ms                                                       | 86.6 ms: 1.26x faster                                                       |
| go                      | 264 ms                                                       | 211 ms: 1.25x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 87.3 ms: 1.25x faster                                                       |
| async_tree_memoization  | 822 ms                                                       | 660 ms: 1.25x faster                                                        |
| chaos                   | 108 ms                                                       | 87.5 ms: 1.23x faster                                                       |
| logging_silent          | 165 ns                                                       | 134 ns: 1.23x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 64.1 ms: 1.21x faster                                                       |
| scimark_sor             | 177 ms                                                       | 147 ms: 1.21x faster                                                        |
| thrift                  | 1.23 ms                                                      | 1.02 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed | 951 ms                                                       | 796 ms: 1.20x faster                                                        |
| pyflate                 | 731 ms                                                       | 615 ms: 1.19x faster                                                        |
| async_generators        | 419 ms                                                       | 356 ms: 1.17x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.41 sec: 1.17x faster                                                      |
| hexiom                  | 9.54 ms                                                      | 8.15 ms: 1.17x faster                                                       |
| pprint_safe_repr        | 1.03 sec                                                     | 879 ms: 1.17x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 102 ms: 1.16x faster                                                        |
| html5lib                | 96.3 ms                                                      | 83.0 ms: 1.16x faster                                                       |
| pprint_pformat          | 2.12 sec                                                     | 1.83 sec: 1.16x faster                                                      |
| gunicorn                | 1.15 ms                                                      | 988 us: 1.16x faster                                                        |
| spectral_norm           | 138 ms                                                       | 120 ms: 1.15x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 394 us: 1.15x faster                                                        |
| richards                | 73.9 ms                                                      | 64.9 ms: 1.14x faster                                                       |
| scimark_lu              | 164 ms                                                       | 145 ms: 1.13x faster                                                        |
| regex_compile           | 191 ms                                                       | 169 ms: 1.13x faster                                                        |
| mako                    | 14.7 ms                                                      | 13.1 ms: 1.13x faster                                                       |
| json_loads              | 30.3 us                                                      | 27.0 us: 1.12x faster                                                       |
| genshi_text             | 31.7 ms                                                      | 28.3 ms: 1.12x faster                                                       |
| tornado_http            | 151 ms                                                       | 136 ms: 1.11x faster                                                        |
| nqueens                 | 114 ms                                                       | 103 ms: 1.10x faster                                                        |
| dask                    | 478 ms                                                       | 433 ms: 1.10x faster                                                        |
| deepcopy_memo           | 49.2 us                                                      | 44.7 us: 1.10x faster                                                       |
| json                    | 5.94 ms                                                      | 5.40 ms: 1.10x faster                                                       |
| django_template         | 52.0 ms                                                      | 47.5 ms: 1.09x faster                                                       |
| xml_etree_generate      | 94.1 ms                                                      | 86.0 ms: 1.09x faster                                                       |
| sqlglot_normalize       | 147 ms                                                       | 135 ms: 1.09x faster                                                        |
| generators              | 57.0 ms                                                      | 52.5 ms: 1.09x faster                                                       |
| unpickle_pure_python    | 318 us                                                       | 293 us: 1.09x faster                                                        |
| dulwich_log             | 80.5 ms                                                      | 74.2 ms: 1.08x faster                                                       |
| scimark_fft             | 359 ms                                                       | 333 ms: 1.08x faster                                                        |
| sqlite_synth            | 2.96 us                                                      | 2.76 us: 1.08x faster                                                       |
| coroutines              | 30.6 ms                                                      | 28.5 ms: 1.07x faster                                                       |
| chameleon               | 9.62 ms                                                      | 8.97 ms: 1.07x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.66 ms: 1.07x faster                                                       |
| 2to3                    | 352 ms                                                       | 329 ms: 1.07x faster                                                        |
| deepcopy                | 457 us                                                       | 427 us: 1.07x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 1.07 ms: 1.07x faster                                                       |
| meteor_contest          | 142 ms                                                       | 133 ms: 1.07x faster                                                        |
| docutils                | 3.41 sec                                                     | 3.22 sec: 1.06x faster                                                      |
| genshi_xml              | 63.5 ms                                                      | 59.9 ms: 1.06x faster                                                       |
| deepcopy_reduce         | 3.91 us                                                      | 3.70 us: 1.06x faster                                                       |
| sympy_expand            | 603 ms                                                       | 573 ms: 1.05x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 66.6 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.84 ms: 1.05x faster                                                       |
| fannkuch                | 496 ms                                                       | 472 ms: 1.05x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 13.6 ms: 1.05x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 26.8 ms: 1.05x faster                                                       |
| sympy_sum               | 193 ms                                                       | 184 ms: 1.05x faster                                                        |
| sympy_str               | 358 ms                                                       | 343 ms: 1.04x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.54 us: 1.04x faster                                                       |
| mdp                     | 2.95 sec                                                     | 2.84 sec: 1.04x faster                                                      |
| pidigits                | 271 ms                                                       | 266 ms: 1.02x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 20.9 ms: 1.02x faster                                                       |
| regex_v8                | 26.0 ms                                                      | 25.6 ms: 1.02x faster                                                       |
| xml_etree_parse         | 160 ms                                                       | 158 ms: 1.01x faster                                                        |
| pickle_list             | 4.11 us                                                      | 4.14 us: 1.01x slower                                                       |
| coverage                | 71.1 ms                                                      | 72.0 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 109 ms                                                       | 111 ms: 1.02x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.05 ms: 1.02x slower                                                       |
| sqlglot_transpile       | 2.69 ms                                                      | 2.76 ms: 1.03x slower                                                       |
| python_startup          | 11.5 ms                                                      | 11.8 ms: 1.03x slower                                                       |
| gc_traversal            | 3.46 ms                                                      | 3.55 ms: 1.03x slower                                                       |
| pickle                  | 10.1 us                                                      | 10.4 us: 1.03x slower                                                       |
| unpickle                | 13.3 us                                                      | 13.7 us: 1.03x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.57 ms: 1.03x slower                                                       |
| create_gc_cycles        | 1.80 ms                                                      | 1.90 ms: 1.06x slower                                                       |
| sqlglot_parse           | 2.24 ms                                                      | 2.37 ms: 1.06x slower                                                       |
| pickle_dict             | 29.5 us                                                      | 31.5 us: 1.07x slower                                                       |
| comprehensions          | 27.3 us                                                      | 29.5 us: 1.08x slower                                                       |
| flaskblogging           | 4.37 ms                                                      | 4.88 ms: 1.12x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.10x faster                                                                |

Benchmark hidden because not significant (2): nbody, regex_dna
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
