
# Results vs. 3.11.0

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 281 ms: 1.03x faster                                                        |
| docutils       | 2.86 sec                                                                  | 2.76 sec: 1.04x faster                                                      |
| html5lib       | 70.2 ms                                                                   | 66.2 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 75.7 ms                                                                   | 73.2 ms: 1.04x faster                                                       |
| pidigits       | 252 ms                                                                    | 250 ms: 1.01x faster                                                        |
| nbody          | 92.1 ms                                                                   | 94.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                                   | 22.3 ms: 1.09x faster                                                       |
| regex_compile  | 154 ms                                                                    | 150 ms: 1.03x faster                                                        |
| regex_dna      | 225 ms                                                                    | 233 ms: 1.03x slower                                                        |
| regex_effbot   | 3.31 ms                                                                   | 3.44 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.3 ms: 1.29x faster                                                       |
| json_loads           | 28.4 us                                                                   | 24.2 us: 1.17x faster                                                       |
| xml_etree_parse      | 161 ms                                                                    | 141 ms: 1.14x faster                                                        |
| unpickle_pure_python | 238 us                                                                    | 212 us: 1.12x faster                                                        |
| pickle_pure_python   | 319 us                                                                    | 316 us: 1.01x faster                                                        |
| unpickle_list        | 4.52 us                                                                   | 4.47 us: 1.01x faster                                                       |
| pickle               | 9.92 us                                                                   | 9.84 us: 1.01x faster                                                       |
| xml_etree_process    | 55.8 ms                                                                   | 55.6 ms: 1.00x faster                                                       |
| unpickle             | 13.0 us                                                                   | 13.1 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 106 ms                                                                    | 108 ms: 1.02x slower                                                        |
| pickle_dict          | 31.1 us                                                                   | 31.9 us: 1.03x slower                                                       |
| pickle_list          | 3.78 us                                                                   | 3.90 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                     | 1.05x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 10.8 ms: 1.01x slower                                                       |
| python_startup_no_site | 7.73 ms                                                                   | 7.86 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                                     | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 57.8 ms                                                                   | 53.5 ms: 1.08x faster                                                       |
| mako           | 10.9 ms                                                                   | 10.4 ms: 1.05x faster                                                       |
| genshi_text    | 26.3 ms                                                                   | 25.8 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                     | 1.04x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:-------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 13.4 ms                                                                   | 10.3 ms: 1.29x faster                                                       |
| mypy2                   | 446 ms                                                                    | 375 ms: 1.19x faster                                                        |
| json_loads              | 28.4 us                                                                   | 24.2 us: 1.17x faster                                                       |
| scimark_lu              | 114 ms                                                                    | 100 ms: 1.14x faster                                                        |
| xml_etree_parse         | 161 ms                                                                    | 141 ms: 1.14x faster                                                        |
| fannkuch                | 449 ms                                                                    | 398 ms: 1.13x faster                                                        |
| unpickle_pure_python    | 238 us                                                                    | 212 us: 1.12x faster                                                        |
| gc_traversal            | 4.22 ms                                                                   | 3.79 ms: 1.11x faster                                                       |
| regex_v8                | 24.4 ms                                                                   | 22.3 ms: 1.09x faster                                                       |
| json                    | 5.59 ms                                                                   | 5.11 ms: 1.09x faster                                                       |
| deltablue               | 3.99 ms                                                                   | 3.67 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 3.73 ms: 1.09x faster                                                       |
| genshi_xml              | 57.8 ms                                                                   | 53.5 ms: 1.08x faster                                                       |
| richards                | 49.1 ms                                                                   | 46.1 ms: 1.06x faster                                                       |
| html5lib                | 70.2 ms                                                                   | 66.2 ms: 1.06x faster                                                       |
| thrift                  | 942 us                                                                    | 894 us: 1.05x faster                                                        |
| coroutines              | 29.5 ms                                                                   | 28.0 ms: 1.05x faster                                                       |
| mako                    | 10.9 ms                                                                   | 10.4 ms: 1.05x faster                                                       |
| hexiom                  | 7.00 ms                                                                   | 6.73 ms: 1.04x faster                                                       |
| crypto_pyaes            | 85.0 ms                                                                   | 81.8 ms: 1.04x faster                                                       |
| pycparser               | 1.30 sec                                                                  | 1.26 sec: 1.04x faster                                                      |
| docutils                | 2.86 sec                                                                  | 2.76 sec: 1.04x faster                                                      |
| dulwich_log             | 69.1 ms                                                                   | 66.7 ms: 1.04x faster                                                       |
| float                   | 75.7 ms                                                                   | 73.2 ms: 1.04x faster                                                       |
| 2to3                    | 289 ms                                                                    | 281 ms: 1.03x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                                   | 1.60 ms: 1.03x faster                                                       |
| logging_silent          | 103 ns                                                                    | 99.7 ns: 1.03x faster                                                       |
| regex_compile           | 154 ms                                                                    | 150 ms: 1.03x faster                                                        |
| async_tree_memoization  | 639 ms                                                                    | 623 ms: 1.03x faster                                                        |
| pprint_pformat          | 1.60 sec                                                                  | 1.56 sec: 1.03x faster                                                      |
| dask                    | 418 ms                                                                    | 409 ms: 1.02x faster                                                        |
| deepcopy_memo           | 37.0 us                                                                   | 36.2 us: 1.02x faster                                                       |
| genshi_text             | 26.3 ms                                                                   | 25.8 ms: 1.02x faster                                                       |
| logging_format          | 7.84 us                                                                   | 7.72 us: 1.02x faster                                                       |
| sympy_expand            | 547 ms                                                                    | 539 ms: 1.01x faster                                                        |
| telco                   | 6.70 ms                                                                   | 6.60 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 768 ms                                                                    | 758 ms: 1.01x faster                                                        |
| asyncio_tcp             | 752 ms                                                                    | 743 ms: 1.01x faster                                                        |
| coverage                | 86.0 ms                                                                   | 85.0 ms: 1.01x faster                                                       |
| pickle_pure_python      | 319 us                                                                    | 316 us: 1.01x faster                                                        |
| unpickle_list           | 4.52 us                                                                   | 4.47 us: 1.01x faster                                                       |
| deepcopy                | 384 us                                                                    | 380 us: 1.01x faster                                                        |
| pathlib                 | 19.2 ms                                                                   | 19.0 ms: 1.01x faster                                                       |
| sqlglot_parse           | 1.53 ms                                                                   | 1.52 ms: 1.01x faster                                                       |
| pickle                  | 9.92 us                                                                   | 9.84 us: 1.01x faster                                                       |
| sqlglot_normalize       | 122 ms                                                                    | 121 ms: 1.01x faster                                                        |
| pidigits                | 252 ms                                                                    | 250 ms: 1.01x faster                                                        |
| sympy_str               | 333 ms                                                                    | 331 ms: 1.00x faster                                                        |
| meteor_contest          | 129 ms                                                                    | 129 ms: 1.00x faster                                                        |
| xml_etree_process       | 55.8 ms                                                                   | 55.6 ms: 1.00x faster                                                       |
| mdp                     | 2.73 sec                                                                  | 2.73 sec: 1.00x slower                                                      |
| python_startup          | 10.7 ms                                                                   | 10.8 ms: 1.01x slower                                                       |
| unpickle                | 13.0 us                                                                   | 13.1 us: 1.01x slower                                                       |
| pyflate                 | 438 ms                                                                    | 440 ms: 1.01x slower                                                        |
| sympy_sum               | 182 ms                                                                    | 183 ms: 1.01x slower                                                        |
| go                      | 158 ms                                                                    | 159 ms: 1.01x slower                                                        |
| sympy_integrate         | 25.3 ms                                                                   | 25.6 ms: 1.01x slower                                                       |
| spectral_norm           | 95.1 ms                                                                   | 96.2 ms: 1.01x slower                                                       |
| logging_simple          | 6.95 us                                                                   | 7.03 us: 1.01x slower                                                       |
| python_startup_no_site  | 7.73 ms                                                                   | 7.86 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 767 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 106 ms                                                                    | 108 ms: 1.02x slower                                                        |
| scimark_fft             | 276 ms                                                                    | 282 ms: 1.02x slower                                                        |
| nbody                   | 92.1 ms                                                                   | 94.3 ms: 1.02x slower                                                       |
| pickle_dict             | 31.1 us                                                                   | 31.9 us: 1.03x slower                                                       |
| chaos                   | 76.2 ms                                                                   | 78.3 ms: 1.03x slower                                                       |
| pickle_list             | 3.78 us                                                                   | 3.90 us: 1.03x slower                                                       |
| regex_dna               | 225 ms                                                                    | 233 ms: 1.03x slower                                                        |
| regex_effbot            | 3.31 ms                                                                   | 3.44 ms: 1.04x slower                                                       |
| sqlite_synth            | 2.49 us                                                                   | 2.60 us: 1.05x slower                                                       |
| async_generators        | 318 ms                                                                    | 335 ms: 1.05x slower                                                        |
| scimark_monte_carlo     | 67.8 ms                                                                   | 72.7 ms: 1.07x slower                                                       |
| raytrace                | 303 ms                                                                    | 327 ms: 1.08x slower                                                        |
| generators              | 56.0 ms                                                                   | 60.8 ms: 1.09x slower                                                       |
| comprehensions          | 24.7 us                                                                   | 27.3 us: 1.10x slower                                                       |
| Geometric mean          | (ref)                                                                     | 1.02x faster                                                                |

Benchmark hidden because not significant (13): bench_mp_pool, unpack_sequence, deepcopy_reduce, async_tree_io, xml_etree_generate, sqlglot_transpile, sqlglot_optimize, django_template, chameleon, scimark_sor, async_tree_none, bench_thread_pool, nqueens
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
