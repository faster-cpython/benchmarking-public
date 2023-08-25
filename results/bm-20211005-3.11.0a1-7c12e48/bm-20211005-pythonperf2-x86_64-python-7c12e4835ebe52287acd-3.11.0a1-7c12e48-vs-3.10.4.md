
# Results vs. 3.10.4

- fork: python
- ref: 7c12e4835ebe52287acd
- machine: linux-x86_64
- commit hash: 7c12e48
- commit date: 2021-10-05
- overall geometric mean: 1.10x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 329 ms: 1.06x faster                                                        |
| chameleon      | 9.72 ms                                                      | 8.97 ms: 1.08x faster                                                       |
| docutils       | 3.40 sec                                                     | 3.22 sec: 1.06x faster                                                      |
| html5lib       | 94.6 ms                                                      | 83.0 ms: 1.14x faster                                                       |
| tornado_http   | 152 ms                                                       | 136 ms: 1.12x faster                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 86.6 ms: 1.27x faster                                                       |
| nbody          | 137 ms                                                       | 132 ms: 1.04x faster                                                        |
| pidigits       | 271 ms                                                       | 266 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 169 ms: 1.15x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 25.6 ms: 1.04x faster                                                       |
| regex_dna      | 259 ms                                                       | 262 ms: 1.01x slower                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.05 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 76.0 ms                                                      | 64.1 ms: 1.19x faster                                                       |
| pickle_pure_python   | 457 us                                                       | 394 us: 1.16x faster                                                        |
| json_loads           | 30.0 us                                                      | 27.0 us: 1.11x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 86.0 ms: 1.10x faster                                                       |
| unpickle_pure_python | 321 us                                                       | 293 us: 1.10x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 13.6 ms: 1.04x faster                                                       |
| unpickle             | 14.2 us                                                      | 13.7 us: 1.04x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 158 ms: 1.02x faster                                                        |
| pickle_list          | 4.11 us                                                      | 4.14 us: 1.01x slower                                                       |
| unpickle_list        | 4.49 us                                                      | 4.54 us: 1.01x slower                                                       |
| pickle               | 9.94 us                                                      | 10.4 us: 1.05x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 31.5 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.8 ms: 1.02x slower                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.57 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 13.1 ms: 1.12x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 28.3 ms: 1.11x faster                                                       |
| django_template | 51.5 ms                                                      | 47.5 ms: 1.08x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 59.9 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| bench_mp_pool           | 7.18 ms                                                      | 5.14 ms: 1.40x faster                                                       |
| async_tree_none         | 700 ms                                                       | 515 ms: 1.36x faster                                                        |
| logging_simple          | 8.90 us                                                      | 6.69 us: 1.33x faster                                                       |
| raytrace                | 488 ms                                                       | 371 ms: 1.32x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.28 us: 1.31x faster                                                       |
| deltablue               | 7.47 ms                                                      | 5.73 ms: 1.30x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.24 sec: 1.29x faster                                                      |
| unpack_sequence         | 59.5 ns                                                      | 46.5 ns: 1.28x faster                                                       |
| float                   | 110 ms                                                       | 86.6 ms: 1.27x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 87.3 ms: 1.25x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 660 ms: 1.25x faster                                                        |
| logging_silent          | 166 ns                                                       | 134 ns: 1.23x faster                                                        |
| go                      | 259 ms                                                       | 211 ms: 1.23x faster                                                        |
| chaos                   | 107 ms                                                       | 87.5 ms: 1.22x faster                                                       |
| scimark_sor             | 177 ms                                                       | 147 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 796 ms: 1.20x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 879 ms: 1.19x faster                                                        |
| gunicorn                | 1.17 ms                                                      | 988 us: 1.19x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 64.1 ms: 1.19x faster                                                       |
| async_generators        | 422 ms                                                       | 356 ms: 1.18x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.41 sec: 1.18x faster                                                      |
| pprint_pformat          | 2.15 sec                                                     | 1.83 sec: 1.18x faster                                                      |
| hexiom                  | 9.52 ms                                                      | 8.15 ms: 1.17x faster                                                       |
| pickle_pure_python      | 457 us                                                       | 394 us: 1.16x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 102 ms: 1.16x faster                                                        |
| regex_compile           | 194 ms                                                       | 169 ms: 1.15x faster                                                        |
| thrift                  | 1.16 ms                                                      | 1.02 ms: 1.14x faster                                                       |
| richards                | 74.1 ms                                                      | 64.9 ms: 1.14x faster                                                       |
| html5lib                | 94.6 ms                                                      | 83.0 ms: 1.14x faster                                                       |
| spectral_norm           | 136 ms                                                       | 120 ms: 1.14x faster                                                        |
| pyflate                 | 697 ms                                                       | 615 ms: 1.13x faster                                                        |
| scimark_lu              | 164 ms                                                       | 145 ms: 1.13x faster                                                        |
| mako                    | 14.7 ms                                                      | 13.1 ms: 1.12x faster                                                       |
| tornado_http            | 152 ms                                                       | 136 ms: 1.12x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 28.3 ms: 1.11x faster                                                       |
| json_loads              | 30.0 us                                                      | 27.0 us: 1.11x faster                                                       |
| generators              | 58.0 ms                                                      | 52.5 ms: 1.10x faster                                                       |
| json                    | 5.96 ms                                                      | 5.40 ms: 1.10x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 86.0 ms: 1.10x faster                                                       |
| unpickle_pure_python    | 321 us                                                       | 293 us: 1.10x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 44.7 us: 1.09x faster                                                       |
| nqueens                 | 112 ms                                                       | 103 ms: 1.09x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.70 us: 1.09x faster                                                       |
| django_template         | 51.5 ms                                                      | 47.5 ms: 1.08x faster                                                       |
| chameleon               | 9.72 ms                                                      | 8.97 ms: 1.08x faster                                                       |
| genshi_xml              | 64.7 ms                                                      | 59.9 ms: 1.08x faster                                                       |
| scimark_fft             | 359 ms                                                       | 333 ms: 1.08x faster                                                        |
| dulwich_log             | 80.1 ms                                                      | 74.2 ms: 1.08x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.76 us: 1.08x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.66 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.84 ms: 1.07x faster                                                       |
| dask                    | 463 ms                                                       | 433 ms: 1.07x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 135 ms: 1.07x faster                                                        |
| coroutines              | 30.4 ms                                                      | 28.5 ms: 1.07x faster                                                       |
| mdp                     | 3.03 sec                                                     | 2.84 sec: 1.07x faster                                                      |
| 2to3                    | 350 ms                                                       | 329 ms: 1.06x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 1.07 ms: 1.06x faster                                                       |
| deepcopy                | 454 us                                                       | 427 us: 1.06x faster                                                        |
| docutils                | 3.40 sec                                                     | 3.22 sec: 1.06x faster                                                      |
| sqlglot_optimize        | 70.3 ms                                                      | 66.6 ms: 1.06x faster                                                       |
| fannkuch                | 496 ms                                                       | 472 ms: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 184 ms: 1.05x faster                                                        |
| sympy_expand            | 599 ms                                                       | 573 ms: 1.05x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 26.8 ms: 1.05x faster                                                       |
| sympy_str               | 358 ms                                                       | 343 ms: 1.04x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 13.6 ms: 1.04x faster                                                       |
| nbody                   | 137 ms                                                       | 132 ms: 1.04x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 25.6 ms: 1.04x faster                                                       |
| unpickle                | 14.2 us                                                      | 13.7 us: 1.04x faster                                                       |
| pathlib                 | 21.7 ms                                                      | 20.9 ms: 1.04x faster                                                       |
| meteor_contest          | 137 ms                                                       | 133 ms: 1.03x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 158 ms: 1.02x faster                                                        |
| pidigits                | 271 ms                                                       | 266 ms: 1.02x faster                                                        |
| pickle_list             | 4.11 us                                                      | 4.14 us: 1.01x slower                                                       |
| regex_dna               | 259 ms                                                       | 262 ms: 1.01x slower                                                        |
| unpickle_list           | 4.49 us                                                      | 4.54 us: 1.01x slower                                                       |
| sqlglot_transpile       | 2.71 ms                                                      | 2.76 ms: 1.02x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.05 ms: 1.02x slower                                                       |
| python_startup          | 11.5 ms                                                      | 11.8 ms: 1.02x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.55 ms: 1.03x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.57 ms: 1.03x slower                                                       |
| create_gc_cycles        | 1.82 ms                                                      | 1.90 ms: 1.05x slower                                                       |
| pickle                  | 9.94 us                                                      | 10.4 us: 1.05x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 31.5 us: 1.05x slower                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 2.37 ms: 1.05x slower                                                       |
| comprehensions          | 26.9 us                                                      | 29.5 us: 1.09x slower                                                       |
| flaskblogging           | 4.39 ms                                                      | 4.88 ms: 1.11x slower                                                       |
| coverage                | 64.0 ms                                                      | 72.0 ms: 1.13x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.10x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x
