
# Results vs. 3.10.4

- fork: faster_cpython
- ref: nogil
- machine: linux-x86_64
- commit hash: 258cab1
- commit date: 2022-12-21
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 382 ms: 1.14x slower                                         |
| chameleon      | 9.17 ms                                                | 8.20 ms: 1.12x faster                                        |
| docutils       | 3.18 sec                                               | 5.20 sec: 1.64x slower                                       |
| html5lib       | 85.9 ms                                                | 81.7 ms: 1.05x faster                                        |
| tornado_http   | 128 ms                                                 | 124 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.09x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 109 ms                                                 | 104 ms: 1.04x faster                                         |
| pidigits       | 190 ms                                                 | 186 ms: 1.02x faster                                         |
| nbody          | 144 ms                                                 | 172 ms: 1.20x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                | 24.1 ms: 1.04x faster                                        |
| regex_dna      | 214 ms                                                 | 218 ms: 1.02x slower                                         |
| regex_effbot   | 3.19 ms                                                | 3.35 ms: 1.05x slower                                        |
| regex_compile  | 177 ms                                                 | 186 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 346 us: 1.31x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 95.5 ms: 1.16x faster                                        |
| unpickle_pure_python | 302 us                                                 | 262 us: 1.15x faster                                         |
| pickle_list          | 4.72 us                                                | 4.17 us: 1.13x faster                                        |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                         |
| pickle_dict          | 27.6 us                                                | 25.3 us: 1.09x faster                                        |
| xml_etree_generate   | 93.8 ms                                                | 87.8 ms: 1.07x faster                                        |
| xml_etree_process    | 74.5 ms                                                | 71.4 ms: 1.04x faster                                        |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                        |
| json_loads           | 28.7 us                                                | 32.5 us: 1.13x slower                                        |
| unpickle_list        | 4.92 us                                                | 5.80 us: 1.18x slower                                        |
| unpickle             | 14.2 us                                                | 18.6 us: 1.31x slower                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.41 ms: 1.50x faster                                        |
| python_startup_no_site | 5.78 ms                                                | 5.91 ms: 1.02x slower                                        |
| Geometric mean         | (ref)                                                  | 1.21x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 42.6 ms: 1.09x faster                                        |
| mako            | 14.7 ms                                                | 16.4 ms: 1.12x slower                                        |
| genshi_xml      | 63.7 ms                                                | 73.6 ms: 1.15x slower                                        |
| genshi_text     | 30.6 ms                                                | 52.1 ms: 1.70x slower                                        |
| Geometric mean  | (ref)                                                  | 1.19x slower                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.78 sec                                               | 829 ms: 2.15x faster                                         |
| richards                | 75.2 ms                                                | 39.3 ms: 1.91x faster                                        |
| async_tree_none         | 711 ms                                                 | 372 ms: 1.91x faster                                         |
| async_tree_memoization  | 855 ms                                                 | 460 ms: 1.86x faster                                         |
| logging_silent          | 176 ns                                                 | 96.0 ns: 1.84x faster                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 614 ms: 1.55x faster                                         |
| python_startup          | 14.1 ms                                                | 9.41 ms: 1.50x faster                                        |
| go                      | 226 ms                                                 | 159 ms: 1.41x faster                                         |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                       |
| scimark_sor             | 197 ms                                                 | 144 ms: 1.36x faster                                         |
| deltablue               | 7.28 ms                                                | 5.41 ms: 1.35x faster                                        |
| pickle_pure_python      | 452 us                                                 | 346 us: 1.31x faster                                         |
| deepcopy_memo           | 51.7 us                                                | 40.1 us: 1.29x faster                                        |
| hexiom                  | 9.43 ms                                                | 7.74 ms: 1.22x faster                                        |
| logging_simple          | 8.10 us                                                | 6.95 us: 1.16x faster                                        |
| xml_etree_iterparse     | 111 ms                                                 | 95.5 ms: 1.16x faster                                        |
| logging_format          | 8.85 us                                                | 7.69 us: 1.15x faster                                        |
| unpickle_pure_python    | 302 us                                                 | 262 us: 1.15x faster                                         |
| unpack_sequence         | 59.4 ns                                                | 52.4 ns: 1.13x faster                                        |
| pycparser               | 1.53 sec                                               | 1.35 sec: 1.13x faster                                       |
| pickle_list             | 4.72 us                                                | 4.17 us: 1.13x faster                                        |
| raytrace                | 467 ms                                                 | 416 ms: 1.12x faster                                         |
| chameleon               | 9.17 ms                                                | 8.20 ms: 1.12x faster                                        |
| deepcopy                | 438 us                                                 | 393 us: 1.11x faster                                         |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                         |
| pickle_dict             | 27.6 us                                                | 25.3 us: 1.09x faster                                        |
| django_template         | 46.3 ms                                                | 42.6 ms: 1.09x faster                                        |
| scimark_monte_carlo     | 109 ms                                                 | 101 ms: 1.08x faster                                         |
| scimark_lu              | 161 ms                                                 | 149 ms: 1.08x faster                                         |
| xml_etree_generate      | 93.8 ms                                                | 87.8 ms: 1.07x faster                                        |
| pyflate                 | 676 ms                                                 | 636 ms: 1.06x faster                                         |
| html5lib                | 85.9 ms                                                | 81.7 ms: 1.05x faster                                        |
| spectral_norm           | 150 ms                                                 | 143 ms: 1.05x faster                                         |
| float                   | 109 ms                                                 | 104 ms: 1.04x faster                                         |
| xml_etree_process       | 74.5 ms                                                | 71.4 ms: 1.04x faster                                        |
| thrift                  | 1.03 ms                                                | 992 us: 1.04x faster                                         |
| deepcopy_reduce         | 3.79 us                                                | 3.63 us: 1.04x faster                                        |
| regex_v8                | 25.0 ms                                                | 24.1 ms: 1.04x faster                                        |
| chaos                   | 106 ms                                                 | 102 ms: 1.04x faster                                         |
| tornado_http            | 128 ms                                                 | 124 ms: 1.03x faster                                         |
| pidigits                | 190 ms                                                 | 186 ms: 1.02x faster                                         |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                        |
| bench_mp_pool           | 24.0 ms                                                | 23.8 ms: 1.01x faster                                        |
| fannkuch                | 488 ms                                                 | 490 ms: 1.00x slower                                         |
| dulwich_log             | 75.8 ms                                                | 77.0 ms: 1.02x slower                                        |
| regex_dna               | 214 ms                                                 | 218 ms: 1.02x slower                                         |
| scimark_fft             | 421 ms                                                 | 430 ms: 1.02x slower                                         |
| python_startup_no_site  | 5.78 ms                                                | 5.91 ms: 1.02x slower                                        |
| pathlib                 | 20.0 ms                                                | 20.6 ms: 1.03x slower                                        |
| sympy_str               | 325 ms                                                 | 335 ms: 1.03x slower                                         |
| crypto_pyaes            | 117 ms                                                 | 122 ms: 1.04x slower                                         |
| regex_effbot            | 3.19 ms                                                | 3.35 ms: 1.05x slower                                        |
| sqlglot_transpile       | 2.43 ms                                                | 2.55 ms: 1.05x slower                                        |
| regex_compile           | 177 ms                                                 | 186 ms: 1.05x slower                                         |
| sympy_integrate         | 24.0 ms                                                | 25.4 ms: 1.06x slower                                        |
| sqlglot_optimize        | 65.2 ms                                                | 69.3 ms: 1.06x slower                                        |
| telco                   | 6.73 ms                                                | 7.15 ms: 1.06x slower                                        |
| gunicorn                | 1.43 ms                                                | 1.52 ms: 1.06x slower                                        |
| generators              | 76.4 ms                                                | 81.6 ms: 1.07x slower                                        |
| sqlglot_parse           | 2.04 ms                                                | 2.18 ms: 1.07x slower                                        |
| aiohttp                 | 1.34 ms                                                | 1.44 ms: 1.07x slower                                        |
| sqlglot_normalize       | 134 ms                                                 | 144 ms: 1.07x slower                                         |
| nqueens                 | 100 ms                                                 | 109 ms: 1.09x slower                                         |
| djangocms               | 36.9 us                                                | 40.5 us: 1.10x slower                                        |
| sqlite_synth            | 2.92 us                                                | 3.24 us: 1.11x slower                                        |
| meteor_contest          | 114 ms                                                 | 127 ms: 1.11x slower                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 6.09 ms: 1.12x slower                                        |
| mako                    | 14.7 ms                                                | 16.4 ms: 1.12x slower                                        |
| mdp                     | 2.74 sec                                               | 3.10 sec: 1.13x slower                                       |
| json_loads              | 28.7 us                                                | 32.5 us: 1.13x slower                                        |
| 2to3                    | 335 ms                                                 | 382 ms: 1.14x slower                                         |
| genshi_xml              | 63.7 ms                                                | 73.6 ms: 1.15x slower                                        |
| sympy_sum               | 183 ms                                                 | 212 ms: 1.16x slower                                         |
| pylint                  | 532 ms                                                 | 626 ms: 1.18x slower                                         |
| unpickle_list           | 4.92 us                                                | 5.80 us: 1.18x slower                                        |
| nbody                   | 144 ms                                                 | 172 ms: 1.20x slower                                         |
| bench_thread_pool       | 946 us                                                 | 1.19 ms: 1.25x slower                                        |
| unpickle                | 14.2 us                                                | 18.6 us: 1.31x slower                                        |
| flaskblogging           | 8.27 ms                                                | 12.1 ms: 1.47x slower                                        |
| async_generators        | 426 ms                                                 | 626 ms: 1.47x slower                                         |
| docutils                | 3.18 sec                                               | 5.20 sec: 1.64x slower                                       |
| genshi_text             | 30.6 ms                                                | 52.1 ms: 1.70x slower                                        |
| coroutines              | 31.6 ms                                                | 72.5 ms: 2.29x slower                                        |
| coverage                | 74.7 ms                                                | 553 ms: 7.39x slower                                         |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (3): sympy_expand, json_dumps, json
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, create_gc_cycles, dask, gc_traversal, mypy2, pprint_safe_repr, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.9.10-258cab1/bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1.json: mypy
