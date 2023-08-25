
# Results vs. 3.11.0

- fork: faster_cpython
- ref: nogil
- machine: linux-x86_64
- commit hash: 258cab1
- commit date: 2022-12-21
- overall geometric mean: 1.24x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 382 ms: 1.47x slower                                         |
| chameleon      | 6.47 ms                                                | 8.20 ms: 1.27x slower                                        |
| docutils       | 2.63 sec                                               | 5.20 sec: 1.98x slower                                       |
| html5lib       | 64.5 ms                                                | 81.7 ms: 1.27x slower                                        |
| tornado_http   | 96.3 ms                                                | 124 ms: 1.29x slower                                         |
| Geometric mean | (ref)                                                  | 1.43x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 186 ms: 1.07x faster                                         |
| float          | 77.2 ms                                                | 104 ms: 1.35x slower                                         |
| nbody          | 93.1 ms                                                | 172 ms: 1.85x slower                                         |
| Geometric mean | (ref)                                                  | 1.33x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.35 ms: 1.19x faster                                        |
| regex_dna      | 204 ms                                                 | 218 ms: 1.07x slower                                         |
| regex_v8       | 22.0 ms                                                | 24.1 ms: 1.09x slower                                        |
| regex_compile  | 138 ms                                                 | 186 ms: 1.35x slower                                         |
| Geometric mean | (ref)                                                  | 1.07x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 25.3 us: 1.23x faster                                        |
| xml_etree_iterparse  | 104 ms                                                 | 95.5 ms: 1.09x faster                                        |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                         |
| pickle_list          | 4.11 us                                                | 4.17 us: 1.01x slower                                        |
| json_dumps           | 12.6 ms                                                | 13.4 ms: 1.07x slower                                        |
| pickle_pure_python   | 306 us                                                 | 346 us: 1.13x slower                                         |
| unpickle_pure_python | 228 us                                                 | 262 us: 1.15x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 87.8 ms: 1.15x slower                                        |
| unpickle_list        | 4.91 us                                                | 5.80 us: 1.18x slower                                        |
| json_loads           | 26.5 us                                                | 32.5 us: 1.23x slower                                        |
| xml_etree_process    | 53.9 ms                                                | 71.4 ms: 1.33x slower                                        |
| unpickle             | 13.7 us                                                | 18.6 us: 1.36x slower                                        |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 5.91 ms: 1.02x faster                                        |
| python_startup         | 8.52 ms                                                | 9.41 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 32.6 ms                                                | 42.6 ms: 1.31x slower                                        |
| genshi_xml      | 51.8 ms                                                | 73.6 ms: 1.42x slower                                        |
| mako            | 10.1 ms                                                | 16.4 ms: 1.63x slower                                        |
| genshi_text     | 21.6 ms                                                | 52.1 ms: 2.42x slower                                        |
| Geometric mean  | (ref)                                                  | 1.64x slower                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.30 sec                                               | 829 ms: 1.56x faster                                         |
| async_tree_none         | 526 ms                                                 | 372 ms: 1.41x faster                                         |
| async_tree_memoization  | 627 ms                                                 | 460 ms: 1.36x faster                                         |
| pickle_dict             | 31.1 us                                                | 25.3 us: 1.23x faster                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 614 ms: 1.20x faster                                         |
| regex_effbot            | 3.99 ms                                                | 3.35 ms: 1.19x faster                                        |
| richards                | 45.7 ms                                                | 39.3 ms: 1.16x faster                                        |
| xml_etree_iterparse     | 104 ms                                                 | 95.5 ms: 1.09x faster                                        |
| pidigits                | 198 ms                                                 | 186 ms: 1.07x faster                                         |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                         |
| logging_silent          | 101 ns                                                 | 96.0 ns: 1.05x faster                                        |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                       |
| python_startup_no_site  | 6.01 ms                                                | 5.91 ms: 1.02x faster                                        |
| bench_mp_pool           | 24.0 ms                                                | 23.8 ms: 1.01x faster                                        |
| pickle_list             | 4.11 us                                                | 4.17 us: 1.01x slower                                        |
| json_dumps              | 12.6 ms                                                | 13.4 ms: 1.07x slower                                        |
| regex_dna               | 204 ms                                                 | 218 ms: 1.07x slower                                         |
| deepcopy_memo           | 37.0 us                                                | 40.1 us: 1.08x slower                                        |
| telco                   | 6.58 ms                                                | 7.15 ms: 1.09x slower                                        |
| json                    | 4.94 ms                                                | 5.37 ms: 1.09x slower                                        |
| regex_v8                | 22.0 ms                                                | 24.1 ms: 1.09x slower                                        |
| python_startup          | 8.52 ms                                                | 9.41 ms: 1.10x slower                                        |
| generators              | 73.5 ms                                                | 81.6 ms: 1.11x slower                                        |
| sympy_expand            | 475 ms                                                 | 531 ms: 1.12x slower                                         |
| pickle_pure_python      | 306 us                                                 | 346 us: 1.13x slower                                         |
| pathlib                 | 18.2 ms                                                | 20.6 ms: 1.13x slower                                        |
| go                      | 140 ms                                                 | 159 ms: 1.14x slower                                         |
| pycparser               | 1.18 sec                                               | 1.35 sec: 1.14x slower                                       |
| deepcopy                | 342 us                                                 | 393 us: 1.15x slower                                         |
| unpickle_pure_python    | 228 us                                                 | 262 us: 1.15x slower                                         |
| logging_format          | 6.68 us                                                | 7.69 us: 1.15x slower                                        |
| xml_etree_generate      | 76.2 ms                                                | 87.8 ms: 1.15x slower                                        |
| logging_simple          | 6.03 us                                                | 6.95 us: 1.15x slower                                        |
| sympy_str               | 290 ms                                                 | 335 ms: 1.16x slower                                         |
| unpickle_list           | 4.91 us                                                | 5.80 us: 1.18x slower                                        |
| mdp                     | 2.62 sec                                               | 3.10 sec: 1.18x slower                                       |
| meteor_contest          | 107 ms                                                 | 127 ms: 1.19x slower                                         |
| dulwich_log             | 63.7 ms                                                | 77.0 ms: 1.21x slower                                        |
| sympy_integrate         | 21.0 ms                                                | 25.4 ms: 1.21x slower                                        |
| hexiom                  | 6.37 ms                                                | 7.74 ms: 1.21x slower                                        |
| unpack_sequence         | 43.1 ns                                                | 52.4 ns: 1.22x slower                                        |
| scimark_sor             | 118 ms                                                 | 144 ms: 1.22x slower                                         |
| json_loads              | 26.5 us                                                | 32.5 us: 1.23x slower                                        |
| deepcopy_reduce         | 2.94 us                                                | 3.63 us: 1.24x slower                                        |
| djangocms               | 32.4 us                                                | 40.5 us: 1.25x slower                                        |
| fannkuch                | 388 ms                                                 | 490 ms: 1.26x slower                                         |
| html5lib                | 64.5 ms                                                | 81.7 ms: 1.27x slower                                        |
| chameleon               | 6.47 ms                                                | 8.20 ms: 1.27x slower                                        |
| sympy_sum               | 167 ms                                                 | 212 ms: 1.27x slower                                         |
| sqlite_synth            | 2.52 us                                                | 3.24 us: 1.29x slower                                        |
| tornado_http            | 96.3 ms                                                | 124 ms: 1.29x slower                                         |
| gunicorn                | 1.18 ms                                                | 1.52 ms: 1.29x slower                                        |
| sqlglot_optimize        | 53.1 ms                                                | 69.3 ms: 1.30x slower                                        |
| aiohttp                 | 1.10 ms                                                | 1.44 ms: 1.30x slower                                        |
| nqueens                 | 83.4 ms                                                | 109 ms: 1.31x slower                                         |
| django_template         | 32.6 ms                                                | 42.6 ms: 1.31x slower                                        |
| scimark_fft             | 328 ms                                                 | 430 ms: 1.31x slower                                         |
| thrift                  | 756 us                                                 | 992 us: 1.31x slower                                         |
| xml_etree_process       | 53.9 ms                                                | 71.4 ms: 1.33x slower                                        |
| sqlglot_normalize       | 108 ms                                                 | 144 ms: 1.34x slower                                         |
| pylint                  | 465 ms                                                 | 626 ms: 1.35x slower                                         |
| regex_compile           | 138 ms                                                 | 186 ms: 1.35x slower                                         |
| float                   | 77.2 ms                                                | 104 ms: 1.35x slower                                         |
| scimark_sparse_mat_mult | 4.50 ms                                                | 6.09 ms: 1.35x slower                                        |
| unpickle                | 13.7 us                                                | 18.6 us: 1.36x slower                                        |
| scimark_lu              | 110 ms                                                 | 149 ms: 1.36x slower                                         |
| raytrace                | 297 ms                                                 | 416 ms: 1.40x slower                                         |
| genshi_xml              | 51.8 ms                                                | 73.6 ms: 1.42x slower                                        |
| spectral_norm           | 100 ms                                                 | 143 ms: 1.43x slower                                         |
| bench_thread_pool       | 819 us                                                 | 1.19 ms: 1.45x slower                                        |
| deltablue               | 3.67 ms                                                | 5.41 ms: 1.47x slower                                        |
| chaos                   | 69.2 ms                                                | 102 ms: 1.47x slower                                         |
| 2to3                    | 259 ms                                                 | 382 ms: 1.47x slower                                         |
| scimark_monte_carlo     | 68.1 ms                                                | 101 ms: 1.48x slower                                         |
| sqlglot_transpile       | 1.70 ms                                                | 2.55 ms: 1.50x slower                                        |
| pyflate                 | 418 ms                                                 | 636 ms: 1.52x slower                                         |
| sqlglot_parse           | 1.40 ms                                                | 2.18 ms: 1.56x slower                                        |
| mako                    | 10.1 ms                                                | 16.4 ms: 1.63x slower                                        |
| crypto_pyaes            | 74.7 ms                                                | 122 ms: 1.63x slower                                         |
| async_generators        | 368 ms                                                 | 626 ms: 1.70x slower                                         |
| flaskblogging           | 7.12 ms                                                | 12.1 ms: 1.71x slower                                        |
| nbody                   | 93.1 ms                                                | 172 ms: 1.85x slower                                         |
| docutils                | 2.63 sec                                               | 5.20 sec: 1.98x slower                                       |
| genshi_text             | 21.6 ms                                                | 52.1 ms: 2.42x slower                                        |
| coroutines              | 25.5 ms                                                | 72.5 ms: 2.84x slower                                        |
| coverage                | 100 ms                                                 | 553 ms: 5.52x slower                                         |
| Geometric mean          | (ref)                                                  | 1.24x slower                                                 |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (13) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2, pprint_safe_repr, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221221-3.9.10-258cab1/bm-20221221-linux-x86_64-faster_cpython-nogil-3.9.10-258cab1.json: mypy


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.16x
