
# Results vs. 3.10.4

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: linux-x86_64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 287 ms: 1.23x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.50 ms: 1.28x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| html5lib       | 96.3 ms                                                      | 73.2 ms: 1.32x faster                                                        |
| tornado_http   | 151 ms                                                       | 125 ms: 1.20x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 132 ms                                                       | 89.6 ms: 1.47x faster                                                        |
| float          | 109 ms                                                       | 75.1 ms: 1.46x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 157 ms: 1.21x faster                                                         |
| regex_dna      | 261 ms                                                       | 225 ms: 1.16x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 24.3 ms: 1.07x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.29 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 451 us                                                       | 324 us: 1.39x faster                                                         |
| xml_etree_process    | 77.6 ms                                                      | 57.0 ms: 1.36x faster                                                        |
| unpickle_pure_python | 318 us                                                       | 250 us: 1.27x faster                                                         |
| xml_etree_generate   | 94.1 ms                                                      | 80.8 ms: 1.16x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.77 us: 1.09x faster                                                        |
| json_loads           | 30.3 us                                                      | 28.4 us: 1.07x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 13.5 ms: 1.06x faster                                                        |
| pickle               | 10.1 us                                                      | 9.61 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| unpickle             | 13.3 us                                                      | 13.0 us: 1.02x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 30.7 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 7.72 ms: 1.05x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| django_template | 52.0 ms                                                      | 39.7 ms: 1.31x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 26.1 ms: 1.21x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 59.2 ms: 1.07x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220911-pythonperf2-x86_64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 4.09 ms: 1.84x faster                                                        |
| logging_silent          | 165 ns                                                       | 101 ns: 1.63x faster                                                         |
| pyflate                 | 731 ms                                                       | 450 ms: 1.63x faster                                                         |
| scimark_sor             | 177 ms                                                       | 110 ms: 1.61x faster                                                         |
| raytrace                | 491 ms                                                       | 307 ms: 1.60x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 68.7 ms: 1.58x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.54 ms: 1.57x faster                                                        |
| go                      | 264 ms                                                       | 172 ms: 1.54x faster                                                         |
| nbody                   | 132 ms                                                       | 89.6 ms: 1.47x faster                                                        |
| float                   | 109 ms                                                       | 75.1 ms: 1.46x faster                                                        |
| spectral_norm           | 138 ms                                                       | 95.5 ms: 1.44x faster                                                        |
| scimark_lu              | 164 ms                                                       | 114 ms: 1.44x faster                                                         |
| sqlglot_parse           | 2.24 ms                                                      | 1.56 ms: 1.44x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 84.3 ms: 1.41x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.92 ms: 1.40x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 324 us: 1.39x faster                                                         |
| richards                | 73.9 ms                                                      | 53.5 ms: 1.38x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                                       |
| xml_etree_process       | 77.6 ms                                                      | 57.0 ms: 1.36x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| thrift                  | 1.23 ms                                                      | 906 us: 1.35x faster                                                         |
| async_tree_none         | 698 ms                                                       | 517 ms: 1.35x faster                                                         |
| hexiom                  | 9.54 ms                                                      | 7.12 ms: 1.34x faster                                                        |
| chaos                   | 108 ms                                                       | 81.4 ms: 1.32x faster                                                        |
| html5lib                | 96.3 ms                                                      | 73.2 ms: 1.32x faster                                                        |
| django_template         | 52.0 ms                                                      | 39.7 ms: 1.31x faster                                                        |
| unpack_sequence         | 59.7 ns                                                      | 45.7 ns: 1.31x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 791 ms: 1.30x faster                                                         |
| scimark_fft             | 359 ms                                                       | 277 ms: 1.29x faster                                                         |
| async_tree_memoization  | 822 ms                                                       | 636 ms: 1.29x faster                                                         |
| pprint_pformat          | 2.12 sec                                                     | 1.65 sec: 1.29x faster                                                       |
| chameleon               | 9.62 ms                                                      | 7.50 ms: 1.28x faster                                                        |
| async_generators        | 419 ms                                                       | 328 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed | 951 ms                                                       | 746 ms: 1.28x faster                                                         |
| unpickle_pure_python    | 318 us                                                       | 250 us: 1.27x faster                                                         |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 4.01 ms: 1.27x faster                                                        |
| logging_simple          | 9.24 us                                                      | 7.43 us: 1.24x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.34 sec: 1.24x faster                                                       |
| logging_format          | 9.94 us                                                      | 8.03 us: 1.24x faster                                                        |
| 2to3                    | 352 ms                                                       | 287 ms: 1.23x faster                                                         |
| aiohttp                 | 1.18 ms                                                      | 966 us: 1.22x faster                                                         |
| gunicorn                | 1.15 ms                                                      | 941 us: 1.22x faster                                                         |
| sqlglot_normalize       | 147 ms                                                       | 121 ms: 1.22x faster                                                         |
| genshi_text             | 31.7 ms                                                      | 26.1 ms: 1.21x faster                                                        |
| regex_compile           | 191 ms                                                       | 157 ms: 1.21x faster                                                         |
| sqlalchemy_declarative  | 188 ms                                                       | 155 ms: 1.21x faster                                                         |
| tornado_http            | 151 ms                                                       | 125 ms: 1.20x faster                                                         |
| deepcopy_memo           | 49.2 us                                                      | 41.0 us: 1.20x faster                                                        |
| docutils                | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                       |
| sqlite_synth            | 2.96 us                                                      | 2.48 us: 1.19x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                                        |
| xml_etree_generate      | 94.1 ms                                                      | 80.8 ms: 1.16x faster                                                        |
| regex_dna               | 261 ms                                                       | 225 ms: 1.16x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 69.6 ms: 1.16x faster                                                        |
| flaskblogging           | 4.37 ms                                                      | 3.80 ms: 1.15x faster                                                        |
| sqlalchemy_imperative   | 22.9 ms                                                      | 19.9 ms: 1.15x faster                                                        |
| dask                    | 478 ms                                                       | 420 ms: 1.14x faster                                                         |
| bench_thread_pool       | 1.14 ms                                                      | 1.00 ms: 1.14x faster                                                        |
| fannkuch                | 496 ms                                                       | 441 ms: 1.13x faster                                                         |
| nqueens                 | 114 ms                                                       | 101 ms: 1.12x faster                                                         |
| deepcopy                | 457 us                                                       | 407 us: 1.12x faster                                                         |
| deepcopy_reduce         | 3.91 us                                                      | 3.51 us: 1.11x faster                                                        |
| pathlib                 | 21.3 ms                                                      | 19.1 ms: 1.11x faster                                                        |
| coroutines              | 30.6 ms                                                      | 27.9 ms: 1.10x faster                                                        |
| sympy_expand            | 603 ms                                                       | 553 ms: 1.09x faster                                                         |
| pickle_list             | 4.11 us                                                      | 3.77 us: 1.09x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.66 ms: 1.09x faster                                                        |
| mdp                     | 2.95 sec                                                     | 2.72 sec: 1.09x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.9 ms: 1.08x faster                                                        |
| pylint                  | 562 ms                                                       | 520 ms: 1.08x faster                                                         |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| genshi_xml              | 63.5 ms                                                      | 59.2 ms: 1.07x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.7 ms: 1.07x faster                                                        |
| meteor_contest          | 142 ms                                                       | 132 ms: 1.07x faster                                                         |
| regex_v8                | 26.0 ms                                                      | 24.3 ms: 1.07x faster                                                        |
| comprehensions          | 27.3 us                                                      | 25.5 us: 1.07x faster                                                        |
| json_loads              | 30.3 us                                                      | 28.4 us: 1.07x faster                                                        |
| json                    | 5.94 ms                                                      | 5.57 ms: 1.07x faster                                                        |
| sympy_str               | 358 ms                                                       | 337 ms: 1.06x faster                                                         |
| json_dumps              | 14.3 ms                                                      | 13.5 ms: 1.06x faster                                                        |
| pickle                  | 10.1 us                                                      | 9.61 us: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                                         |
| xml_etree_iterparse     | 109 ms                                                       | 104 ms: 1.05x faster                                                         |
| generators              | 57.0 ms                                                      | 54.2 ms: 1.05x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 752 ms: 1.05x faster                                                         |
| telco                   | 7.14 ms                                                      | 6.88 ms: 1.04x faster                                                        |
| unpickle                | 13.3 us                                                      | 13.0 us: 1.02x faster                                                        |
| pickle_dict             | 29.5 us                                                      | 30.7 us: 1.04x slower                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.63 ms: 1.05x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.72 ms: 1.05x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.29 ms: 1.10x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.21x faster                                                                 |

Benchmark hidden because not significant (3): mypy2, unpickle_list, xml_etree_parse
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage
