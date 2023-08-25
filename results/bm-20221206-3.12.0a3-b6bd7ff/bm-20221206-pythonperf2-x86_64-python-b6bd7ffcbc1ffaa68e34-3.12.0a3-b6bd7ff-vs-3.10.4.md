
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| chameleon      | 9.72 ms                                                      | 7.51 ms: 1.30x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.76 sec: 1.23x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 73.2 ms: 1.51x faster                                                       |
| nbody          | 137 ms                                                       | 94.3 ms: 1.46x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 150 ms: 1.29x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 22.3 ms: 1.19x faster                                                       |
| regex_dna      | 259 ms                                                       | 233 ms: 1.11x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 212 us: 1.51x faster                                                        |
| pickle_pure_python   | 457 us                                                       | 316 us: 1.45x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.3 ms: 1.37x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 55.6 ms: 1.37x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 78.9 ms: 1.20x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 141 ms: 1.15x faster                                                        |
| unpickle             | 14.2 us                                                      | 13.1 us: 1.08x faster                                                       |
| pickle_list          | 4.11 us                                                      | 3.90 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 108 ms: 1.03x faster                                                        |
| pickle               | 9.94 us                                                      | 9.84 us: 1.01x faster                                                       |
| pickle_dict          | 30.0 us                                                      | 31.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

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
| django_template | 51.5 ms                                                      | 39.6 ms: 1.30x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 25.8 ms: 1.22x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 53.5 ms: 1.21x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-pythonperf2-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.67 ms: 2.04x faster                                                       |
| logging_silent          | 166 ns                                                       | 99.7 ns: 1.66x faster                                                       |
| scimark_lu              | 164 ms                                                       | 100 ms: 1.63x faster                                                        |
| go                      | 259 ms                                                       | 159 ms: 1.63x faster                                                        |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.62x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.46 ms: 1.61x faster                                                       |
| richards                | 74.1 ms                                                      | 46.1 ms: 1.61x faster                                                       |
| pyflate                 | 697 ms                                                       | 440 ms: 1.58x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 212 us: 1.51x faster                                                        |
| float                   | 110 ms                                                       | 73.2 ms: 1.51x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 72.7 ms: 1.51x faster                                                       |
| raytrace                | 488 ms                                                       | 327 ms: 1.49x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.52 ms: 1.49x faster                                                       |
| nbody                   | 137 ms                                                       | 94.3 ms: 1.46x faster                                                       |
| pickle_pure_python      | 457 us                                                       | 316 us: 1.45x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.87 ms: 1.45x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 81.8 ms: 1.45x faster                                                       |
| html5lib                | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| spectral_norm           | 136 ms                                                       | 96.2 ms: 1.42x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 6.73 ms: 1.41x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.73 ms: 1.39x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 758 ms: 1.38x faster                                                        |
| pprint_pformat          | 2.15 sec                                                     | 1.56 sec: 1.38x faster                                                      |
| json_dumps              | 14.2 ms                                                      | 10.3 ms: 1.37x faster                                                       |
| chaos                   | 107 ms                                                       | 78.3 ms: 1.37x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 55.6 ms: 1.37x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.18 sec: 1.36x faster                                                      |
| deepcopy_memo           | 48.9 us                                                      | 36.2 us: 1.35x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                      |
| async_tree_memoization  | 824 ms                                                       | 623 ms: 1.32x faster                                                        |
| async_tree_none         | 700 ms                                                       | 531 ms: 1.32x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 45.5 ns: 1.31x faster                                                       |
| thrift                  | 1.16 ms                                                      | 894 us: 1.30x faster                                                        |
| django_template         | 51.5 ms                                                      | 39.6 ms: 1.30x faster                                                       |
| chameleon               | 9.72 ms                                                      | 7.51 ms: 1.30x faster                                                       |
| regex_compile           | 194 ms                                                       | 150 ms: 1.29x faster                                                        |
| scimark_fft             | 359 ms                                                       | 282 ms: 1.27x faster                                                        |
| logging_simple          | 8.90 us                                                      | 7.03 us: 1.27x faster                                                       |
| async_generators        | 422 ms                                                       | 335 ms: 1.26x faster                                                        |
| 2to3                    | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| fannkuch                | 496 ms                                                       | 398 ms: 1.24x faster                                                        |
| mypy2                   | 466 ms                                                       | 375 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 767 ms: 1.24x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.72 us: 1.24x faster                                                       |
| json_loads              | 30.0 us                                                      | 24.2 us: 1.24x faster                                                       |
| docutils                | 3.40 sec                                                     | 2.76 sec: 1.23x faster                                                      |
| genshi_text             | 31.5 ms                                                      | 25.8 ms: 1.22x faster                                                       |
| genshi_xml              | 64.7 ms                                                      | 53.5 ms: 1.21x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 58.5 ms: 1.20x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 66.7 ms: 1.20x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 78.9 ms: 1.20x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.37 us: 1.20x faster                                                       |
| deepcopy                | 454 us                                                       | 380 us: 1.20x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 22.3 ms: 1.19x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 121 ms: 1.19x faster                                                        |
| json                    | 5.96 ms                                                      | 5.11 ms: 1.17x faster                                                       |
| xml_etree_parse         | 162 ms                                                       | 141 ms: 1.15x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 994 us: 1.14x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.0 ms: 1.14x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.60 us: 1.14x faster                                                       |
| create_gc_cycles        | 1.82 ms                                                      | 1.60 ms: 1.14x faster                                                       |
| dask                    | 463 ms                                                       | 409 ms: 1.13x faster                                                        |
| regex_dna               | 259 ms                                                       | 233 ms: 1.11x faster                                                        |
| sympy_expand            | 599 ms                                                       | 539 ms: 1.11x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.73 sec: 1.11x faster                                                      |
| nqueens                 | 112 ms                                                       | 102 ms: 1.10x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 25.6 ms: 1.10x faster                                                       |
| coroutines              | 30.4 ms                                                      | 28.0 ms: 1.09x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.60 ms: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.1 us: 1.08x faster                                                       |
| sympy_str               | 358 ms                                                       | 331 ms: 1.08x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.06x faster                                                       |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.90 us: 1.05x faster                                                       |
| asyncio_tcp             | 782 ms                                                       | 743 ms: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 183 ms: 1.05x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 108 ms: 1.03x faster                                                        |
| pickle                  | 9.94 us                                                      | 9.84 us: 1.01x faster                                                       |
| comprehensions          | 26.9 us                                                      | 27.3 us: 1.01x slower                                                       |
| generators              | 58.0 ms                                                      | 60.8 ms: 1.05x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 31.9 us: 1.06x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.86 ms: 1.07x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.79 ms: 1.10x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.44 ms: 1.15x slower                                                       |
| coverage                | 64.0 ms                                                      | 85.0 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.24x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x
