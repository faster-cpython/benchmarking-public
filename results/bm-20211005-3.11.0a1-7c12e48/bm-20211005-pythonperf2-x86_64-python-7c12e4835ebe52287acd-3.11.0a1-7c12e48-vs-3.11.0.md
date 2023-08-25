
# Results vs. 3.11.0

- fork: python
- ref: 7c12e4835ebe52287acd
- machine: linux-x86_64
- commit hash: 7c12e48
- commit date: 2021-10-05
- overall geometric mean: 1.10x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 329 ms: 1.14x slower                                                        |
| chameleon      | 7.67 ms                                                      | 8.97 ms: 1.17x slower                                                       |
| docutils       | 2.86 sec                                                     | 3.22 sec: 1.13x slower                                                      |
| html5lib       | 72.9 ms                                                      | 83.0 ms: 1.14x slower                                                       |
| tornado_http   | 122 ms                                                       | 136 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 266 ms: 1.06x slower                                                        |
| float          | 74.2 ms                                                      | 86.6 ms: 1.17x slower                                                       |
| nbody          | 90.7 ms                                                      | 132 ms: 1.46x slower                                                        |
| Geometric mean | (ref)                                                        | 1.22x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.05 ms: 1.15x faster                                                       |
| regex_v8       | 23.9 ms                                                      | 25.6 ms: 1.07x slower                                                       |
| regex_compile  | 158 ms                                                       | 169 ms: 1.07x slower                                                        |
| regex_dna      | 227 ms                                                       | 262 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                      | 27.0 us: 1.06x faster                                                       |
| unpickle             | 13.4 us                                                      | 13.7 us: 1.02x slower                                                       |
| json_dumps           | 13.4 ms                                                      | 13.6 ms: 1.02x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 31.5 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 104 ms                                                       | 111 ms: 1.07x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 86.0 ms: 1.07x slower                                                       |
| pickle_list          | 3.83 us                                                      | 4.14 us: 1.08x slower                                                       |
| pickle               | 9.64 us                                                      | 10.4 us: 1.08x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 64.1 ms: 1.14x slower                                                       |
| unpickle_pure_python | 241 us                                                       | 293 us: 1.22x slower                                                        |
| pickle_pure_python   | 319 us                                                       | 394 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.57 ms: 1.02x faster                                                       |
| python_startup         | 10.8 ms                                                      | 11.8 ms: 1.09x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 59.9 ms: 1.02x slower                                                       |
| genshi_text     | 26.1 ms                                                      | 28.3 ms: 1.08x slower                                                       |
| django_template | 40.2 ms                                                      | 47.5 ms: 1.18x slower                                                       |
| mako            | 11.0 ms                                                      | 13.1 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211005-pythonperf2-x86_64-python-7c12e4835ebe52287acd-3.11.0a1-7c12e48 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coverage                | 84.8 ms                                                      | 72.0 ms: 1.18x faster                                                       |
| regex_effbot            | 3.50 ms                                                      | 3.05 ms: 1.15x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.28 us: 1.11x faster                                                       |
| gc_traversal            | 3.85 ms                                                      | 3.55 ms: 1.08x faster                                                       |
| logging_simple          | 7.19 us                                                      | 6.69 us: 1.08x faster                                                       |
| generators              | 56.0 ms                                                      | 52.5 ms: 1.07x faster                                                       |
| json_loads              | 28.7 us                                                      | 27.0 us: 1.06x faster                                                       |
| json                    | 5.65 ms                                                      | 5.40 ms: 1.05x faster                                                       |
| telco                   | 6.86 ms                                                      | 6.66 ms: 1.03x faster                                                       |
| python_startup_no_site  | 7.76 ms                                                      | 7.57 ms: 1.02x faster                                                       |
| sympy_sum               | 185 ms                                                       | 184 ms: 1.00x faster                                                        |
| gunicorn                | 973 us                                                       | 988 us: 1.02x slower                                                        |
| sympy_str               | 337 ms                                                       | 343 ms: 1.02x slower                                                        |
| unpickle                | 13.4 us                                                      | 13.7 us: 1.02x slower                                                       |
| json_dumps              | 13.4 ms                                                      | 13.6 ms: 1.02x slower                                                       |
| meteor_contest          | 131 ms                                                       | 133 ms: 1.02x slower                                                        |
| unpack_sequence         | 45.6 ns                                                      | 46.5 ns: 1.02x slower                                                       |
| genshi_xml              | 58.5 ms                                                      | 59.9 ms: 1.02x slower                                                       |
| pickle_dict             | 30.8 us                                                      | 31.5 us: 1.02x slower                                                       |
| sympy_expand            | 555 ms                                                       | 573 ms: 1.03x slower                                                        |
| coroutines              | 27.6 ms                                                      | 28.5 ms: 1.03x slower                                                       |
| mdp                     | 2.75 sec                                                     | 2.84 sec: 1.04x slower                                                      |
| sympy_integrate         | 25.8 ms                                                      | 26.8 ms: 1.04x slower                                                       |
| async_tree_memoization  | 630 ms                                                       | 660 ms: 1.05x slower                                                        |
| deepcopy_reduce         | 3.51 us                                                      | 3.70 us: 1.05x slower                                                       |
| dask                    | 410 ms                                                       | 433 ms: 1.06x slower                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 1.07 ms: 1.06x slower                                                       |
| pidigits                | 251 ms                                                       | 266 ms: 1.06x slower                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.24 sec: 1.06x slower                                                      |
| async_tree_cpu_io_mixed | 749 ms                                                       | 796 ms: 1.06x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 111 ms: 1.07x slower                                                        |
| pycparser               | 1.32 sec                                                     | 1.41 sec: 1.07x slower                                                      |
| xml_etree_generate      | 80.5 ms                                                      | 86.0 ms: 1.07x slower                                                       |
| deepcopy                | 399 us                                                       | 427 us: 1.07x slower                                                        |
| regex_v8                | 23.9 ms                                                      | 25.6 ms: 1.07x slower                                                       |
| regex_compile           | 158 ms                                                       | 169 ms: 1.07x slower                                                        |
| sqlglot_normalize       | 126 ms                                                       | 135 ms: 1.07x slower                                                        |
| pickle_list             | 3.83 us                                                      | 4.14 us: 1.08x slower                                                       |
| pickle                  | 9.64 us                                                      | 10.4 us: 1.08x slower                                                       |
| genshi_text             | 26.1 ms                                                      | 28.3 ms: 1.08x slower                                                       |
| chaos                   | 80.9 ms                                                      | 87.5 ms: 1.08x slower                                                       |
| dulwich_log             | 68.4 ms                                                      | 74.2 ms: 1.08x slower                                                       |
| python_startup          | 10.8 ms                                                      | 11.8 ms: 1.09x slower                                                       |
| pathlib                 | 19.1 ms                                                      | 20.9 ms: 1.10x slower                                                       |
| thrift                  | 925 us                                                       | 1.02 ms: 1.10x slower                                                       |
| fannkuch                | 429 ms                                                       | 472 ms: 1.10x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.76 us: 1.10x slower                                                       |
| bench_mp_pool           | 4.62 ms                                                      | 5.14 ms: 1.11x slower                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 66.6 ms: 1.11x slower                                                       |
| tornado_http            | 122 ms                                                       | 136 ms: 1.12x slower                                                        |
| pprint_safe_repr        | 784 ms                                                       | 879 ms: 1.12x slower                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.83 sec: 1.12x slower                                                      |
| docutils                | 2.86 sec                                                     | 3.22 sec: 1.13x slower                                                      |
| async_generators        | 316 ms                                                       | 356 ms: 1.13x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 64.1 ms: 1.14x slower                                                       |
| html5lib                | 72.9 ms                                                      | 83.0 ms: 1.14x slower                                                       |
| hexiom                  | 7.13 ms                                                      | 8.15 ms: 1.14x slower                                                       |
| 2to3                    | 288 ms                                                       | 329 ms: 1.14x slower                                                        |
| deepcopy_memo           | 38.8 us                                                      | 44.7 us: 1.15x slower                                                       |
| regex_dna               | 227 ms                                                       | 262 ms: 1.15x slower                                                        |
| float                   | 74.2 ms                                                      | 86.6 ms: 1.17x slower                                                       |
| scimark_fft             | 285 ms                                                       | 333 ms: 1.17x slower                                                        |
| chameleon               | 7.67 ms                                                      | 8.97 ms: 1.17x slower                                                       |
| raytrace                | 317 ms                                                       | 371 ms: 1.17x slower                                                        |
| django_template         | 40.2 ms                                                      | 47.5 ms: 1.18x slower                                                       |
| create_gc_cycles        | 1.61 ms                                                      | 1.90 ms: 1.18x slower                                                       |
| mako                    | 11.0 ms                                                      | 13.1 ms: 1.19x slower                                                       |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.84 ms: 1.20x slower                                                       |
| comprehensions          | 24.6 us                                                      | 29.5 us: 1.20x slower                                                       |
| unpickle_pure_python    | 241 us                                                       | 293 us: 1.22x slower                                                        |
| crypto_pyaes            | 83.4 ms                                                      | 102 ms: 1.22x slower                                                        |
| pickle_pure_python      | 319 us                                                       | 394 us: 1.23x slower                                                        |
| flaskblogging           | 3.88 ms                                                      | 4.88 ms: 1.26x slower                                                       |
| scimark_lu              | 115 ms                                                       | 145 ms: 1.27x slower                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 87.3 ms: 1.28x slower                                                       |
| spectral_norm           | 93.3 ms                                                      | 120 ms: 1.29x slower                                                        |
| go                      | 164 ms                                                       | 211 ms: 1.29x slower                                                        |
| scimark_sor             | 111 ms                                                       | 147 ms: 1.32x slower                                                        |
| logging_silent          | 101 ns                                                       | 134 ns: 1.33x slower                                                        |
| richards                | 48.3 ms                                                      | 64.9 ms: 1.34x slower                                                       |
| pyflate                 | 449 ms                                                       | 615 ms: 1.37x slower                                                        |
| deltablue               | 4.00 ms                                                      | 5.73 ms: 1.43x slower                                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 2.76 ms: 1.44x slower                                                       |
| nbody                   | 90.7 ms                                                      | 132 ms: 1.46x slower                                                        |
| sqlglot_parse           | 1.53 ms                                                      | 2.37 ms: 1.55x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.10x slower                                                                |

Benchmark hidden because not significant (4): async_tree_none, nqueens, unpickle_list, xml_etree_parse
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x
