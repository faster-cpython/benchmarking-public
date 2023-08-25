
# Results vs. 3.10.4

- fork: python
- ref: 2e91dba437fe5c56c6f8
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.15x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.19x faster                                                        |
| chameleon      | 9.72 ms                                                      | 8.85 ms: 1.10x faster                                                       |
| docutils       | 3.40 sec                                                     | 3.02 sec: 1.13x faster                                                      |
| html5lib       | 94.6 ms                                                      | 75.1 ms: 1.26x faster                                                       |
| tornado_http   | 152 ms                                                       | 135 ms: 1.13x faster                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 80.9 ms: 1.36x faster                                                       |
| nbody          | 137 ms                                                       | 109 ms: 1.26x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 153 ms: 1.27x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                                       |
| regex_dna      | 259 ms                                                       | 261 ms: 1.01x slower                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.10 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 76.0 ms                                                      | 60.9 ms: 1.25x faster                                                       |
| pickle_pure_python   | 457 us                                                       | 366 us: 1.25x faster                                                        |
| unpickle_pure_python | 321 us                                                       | 265 us: 1.21x faster                                                        |
| json_loads           | 30.0 us                                                      | 25.3 us: 1.18x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 82.8 ms: 1.14x faster                                                       |
| unpickle             | 14.2 us                                                      | 13.2 us: 1.07x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 155 ms: 1.04x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 14.1 ms: 1.01x faster                                                       |
| unpickle_list        | 4.49 us                                                      | 4.53 us: 1.01x slower                                                       |
| pickle               | 9.94 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.32 us: 1.05x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 33.0 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.1 ms: 1.14x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.14 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 51.5 ms                                                      | 44.9 ms: 1.15x faster                                                       |
| mako            | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 28.2 ms: 1.11x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 59.7 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-pythonperf2-x86_64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 4.78 ms: 1.56x faster                                                       |
| scimark_sor             | 177 ms                                                       | 115 ms: 1.53x faster                                                        |
| go                      | 259 ms                                                       | 173 ms: 1.50x faster                                                        |
| scimark_lu              | 164 ms                                                       | 110 ms: 1.49x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.90 ms: 1.46x faster                                                       |
| logging_silent          | 166 ns                                                       | 116 ns: 1.43x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 76.7 ms: 1.43x faster                                                       |
| raytrace                | 488 ms                                                       | 347 ms: 1.41x faster                                                        |
| chaos                   | 107 ms                                                       | 78.3 ms: 1.37x faster                                                       |
| spectral_norm           | 136 ms                                                       | 99.9 ms: 1.36x faster                                                       |
| float                   | 110 ms                                                       | 80.9 ms: 1.36x faster                                                       |
| pyflate                 | 697 ms                                                       | 525 ms: 1.33x faster                                                        |
| async_generators        | 422 ms                                                       | 319 ms: 1.32x faster                                                        |
| richards                | 74.1 ms                                                      | 56.7 ms: 1.31x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 7.41 ms: 1.28x faster                                                       |
| unpack_sequence         | 59.5 ns                                                      | 46.3 ns: 1.28x faster                                                       |
| async_tree_none         | 700 ms                                                       | 545 ms: 1.28x faster                                                        |
| regex_compile           | 194 ms                                                       | 153 ms: 1.27x faster                                                        |
| nbody                   | 137 ms                                                       | 109 ms: 1.26x faster                                                        |
| logging_simple          | 8.90 us                                                      | 7.04 us: 1.26x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 832 ms: 1.26x faster                                                        |
| html5lib                | 94.6 ms                                                      | 75.1 ms: 1.26x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 60.9 ms: 1.25x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 94.7 ms: 1.25x faster                                                       |
| pickle_pure_python      | 457 us                                                       | 366 us: 1.25x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.70 us: 1.24x faster                                                       |
| pprint_pformat          | 2.15 sec                                                     | 1.74 sec: 1.24x faster                                                      |
| pycparser               | 1.66 sec                                                     | 1.35 sec: 1.23x faster                                                      |
| async_tree_io           | 1.61 sec                                                     | 1.32 sec: 1.22x faster                                                      |
| unpickle_pure_python    | 321 us                                                       | 265 us: 1.21x faster                                                        |
| async_tree_memoization  | 824 ms                                                       | 686 ms: 1.20x faster                                                        |
| 2to3                    | 350 ms                                                       | 293 ms: 1.19x faster                                                        |
| json_loads              | 30.0 us                                                      | 25.3 us: 1.18x faster                                                       |
| deepcopy_memo           | 48.9 us                                                      | 41.5 us: 1.18x faster                                                       |
| async_tree_cpu_io_mixed | 952 ms                                                       | 811 ms: 1.17x faster                                                        |
| gunicorn                | 1.17 ms                                                      | 1.00 ms: 1.17x faster                                                       |
| thrift                  | 1.16 ms                                                      | 995 us: 1.17x faster                                                        |
| fannkuch                | 496 ms                                                       | 428 ms: 1.16x faster                                                        |
| generators              | 58.0 ms                                                      | 50.1 ms: 1.16x faster                                                       |
| django_template         | 51.5 ms                                                      | 44.9 ms: 1.15x faster                                                       |
| scimark_fft             | 359 ms                                                       | 314 ms: 1.15x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 82.8 ms: 1.14x faster                                                       |
| mako                    | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                       |
| json                    | 5.96 ms                                                      | 5.24 ms: 1.14x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.1 ms: 1.14x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.55 us: 1.13x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.58 ms: 1.13x faster                                                       |
| tornado_http            | 152 ms                                                       | 135 ms: 1.13x faster                                                        |
| coroutines              | 30.4 ms                                                      | 27.0 ms: 1.13x faster                                                       |
| docutils                | 3.40 sec                                                     | 3.02 sec: 1.13x faster                                                      |
| genshi_text             | 31.5 ms                                                      | 28.2 ms: 1.11x faster                                                       |
| chameleon               | 9.72 ms                                                      | 8.85 ms: 1.10x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.70 us: 1.10x faster                                                       |
| create_gc_cycles        | 1.82 ms                                                      | 1.66 ms: 1.10x faster                                                       |
| mdp                     | 3.03 sec                                                     | 2.76 sec: 1.10x faster                                                      |
| dulwich_log             | 80.1 ms                                                      | 73.0 ms: 1.10x faster                                                       |
| nqueens                 | 112 ms                                                       | 103 ms: 1.09x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 133 ms: 1.09x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.9 ms: 1.09x faster                                                       |
| deepcopy                | 454 us                                                       | 418 us: 1.09x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 64.7 ms: 1.09x faster                                                       |
| genshi_xml              | 64.7 ms                                                      | 59.7 ms: 1.08x faster                                                       |
| unpickle                | 14.2 us                                                      | 13.2 us: 1.07x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 1.06 ms: 1.07x faster                                                       |
| pidigits                | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| dask                    | 463 ms                                                       | 435 ms: 1.06x faster                                                        |
| meteor_contest          | 137 ms                                                       | 129 ms: 1.06x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 26.5 ms: 1.06x faster                                                       |
| sqlglot_transpile       | 2.71 ms                                                      | 2.60 ms: 1.04x faster                                                       |
| xml_etree_parse         | 162 ms                                                       | 155 ms: 1.04x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 25.7 ms: 1.04x faster                                                       |
| sympy_expand            | 599 ms                                                       | 579 ms: 1.03x faster                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 7.14 ms: 1.03x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 2.21 ms: 1.02x faster                                                       |
| sympy_str               | 358 ms                                                       | 350 ms: 1.02x faster                                                        |
| sympy_sum               | 193 ms                                                       | 189 ms: 1.02x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 14.1 ms: 1.01x faster                                                       |
| regex_dna               | 259 ms                                                       | 261 ms: 1.01x slower                                                        |
| unpickle_list           | 4.49 us                                                      | 4.53 us: 1.01x slower                                                       |
| pickle                  | 9.94 us                                                      | 10.2 us: 1.03x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.10 ms: 1.04x slower                                                       |
| pickle_list             | 4.11 us                                                      | 4.32 us: 1.05x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 33.0 us: 1.10x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.89 ms: 1.13x slower                                                       |
| coverage                | 64.0 ms                                                      | 72.1 ms: 1.13x slower                                                       |
| flaskblogging           | 4.39 ms                                                      | 4.95 ms: 1.13x slower                                                       |
| comprehensions          | 26.9 us                                                      | 30.6 us: 1.13x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.15x faster                                                                |

Benchmark hidden because not significant (2): telco, xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x
