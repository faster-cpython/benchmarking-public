# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.02x faster
- HPT reliability: 97.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                                                                         | 291 ms: 1.05x faster                                                                                       |
| chameleon      | 7.48 ms                                                                                                        | 7.40 ms: 1.01x faster                                                                                      |
| html5lib       | 75.4 ms                                                                                                        | 74.7 ms: 1.01x faster                                                                                      |
| tornado_http   | 123 ms                                                                                                         | 119 ms: 1.03x faster                                                                                       |
| Geometric mean | (ref)                                                                                                          | 1.02x faster                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_io             | 921 ms                                                                                                         | 873 ms: 1.05x faster                                                                                       |
| async_tree_memoization_tg | 441 ms                                                                                                         | 421 ms: 1.05x faster                                                                                       |
| async_tree_cpu_io_mixed   | 628 ms                                                                                                         | 604 ms: 1.04x faster                                                                                       |
| async_tree_none           | 380 ms                                                                                                         | 365 ms: 1.04x faster                                                                                       |
| Geometric mean            | (ref)                                                                                                          | 1.02x faster                                                                                               |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pidigits       | 250 ms                                                                                                         | 254 ms: 1.01x slower                                                                                       |
| nbody          | 82.9 ms                                                                                                        | 87.8 ms: 1.06x slower                                                                                      |
| float          | 74.2 ms                                                                                                        | 80.2 ms: 1.08x slower                                                                                      |
| Geometric mean | (ref)                                                                                                          | 1.05x slower                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.56 ms                                                                                                        | 3.40 ms: 1.05x faster                                                                                      |
| regex_dna      | 248 ms                                                                                                         | 249 ms: 1.00x slower                                                                                       |
| regex_v8       | 25.2 ms                                                                                                        | 26.0 ms: 1.03x slower                                                                                      |
| regex_compile  | 139 ms                                                                                                         | 144 ms: 1.04x slower                                                                                       |
| Geometric mean | (ref)                                                                                                          | 1.01x slower                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 4.75 us                                                                                                        | 4.70 us: 1.01x faster                                                                                      |
| xml_etree_parse      | 145 ms                                                                                                         | 144 ms: 1.01x faster                                                                                       |
| pickle_pure_python   | 310 us                                                                                                         | 307 us: 1.01x faster                                                                                       |
| json_dumps           | 10.7 ms                                                                                                        | 10.8 ms: 1.01x slower                                                                                      |
| xml_etree_process    | 58.5 ms                                                                                                        | 59.7 ms: 1.02x slower                                                                                      |
| pickle_list          | 4.35 us                                                                                                        | 4.44 us: 1.02x slower                                                                                      |
| json_loads           | 24.4 us                                                                                                        | 25.0 us: 1.03x slower                                                                                      |
| xml_etree_iterparse  | 99.3 ms                                                                                                        | 103 ms: 1.03x slower                                                                                       |
| xml_etree_generate   | 82.4 ms                                                                                                        | 85.7 ms: 1.04x slower                                                                                      |
| unpickle_pure_python | 211 us                                                                                                         | 224 us: 1.06x slower                                                                                       |
| pickle_dict          | 30.9 us                                                                                                        | 32.8 us: 1.06x slower                                                                                      |
| tomli_loads          | 2.09 sec                                                                                                       | 2.40 sec: 1.15x slower                                                                                     |
| Geometric mean       | (ref)                                                                                                          | 1.03x slower                                                                                               |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.44 ms                                                                                                        | 8.85 ms: 1.07x faster                                                                                      |
| python_startup         | 13.8 ms                                                                                                        | 13.2 ms: 1.05x faster                                                                                      |
| Geometric mean         | (ref)                                                                                                          | 1.06x faster                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 65.3 ms                                                                                                        | 58.1 ms: 1.13x faster                                                                                      |
| genshi_text     | 28.2 ms                                                                                                        | 25.9 ms: 1.09x faster                                                                                      |
| django_template | 41.4 ms                                                                                                        | 39.0 ms: 1.06x faster                                                                                      |
| mako            | 9.10 ms                                                                                                        | 10.4 ms: 1.14x slower                                                                                      |
| Geometric mean  | (ref)                                                                                                          | 1.03x faster                                                                                               |

All benchmarks:
===============

| Benchmark                 | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| logging_silent            | 123 ns                                                                                                         | 96.3 ns: 1.28x faster                                                                                      |
| scimark_sor               | 144 ms                                                                                                         | 119 ms: 1.21x faster                                                                                       |
| scimark_lu                | 114 ms                                                                                                         | 97.5 ms: 1.17x faster                                                                                      |
| raytrace                  | 297 ms                                                                                                         | 260 ms: 1.14x faster                                                                                       |
| deltablue                 | 3.81 ms                                                                                                        | 3.37 ms: 1.13x faster                                                                                      |
| genshi_xml                | 65.3 ms                                                                                                        | 58.1 ms: 1.13x faster                                                                                      |
| mypy2                     | 852 ms                                                                                                         | 764 ms: 1.11x faster                                                                                       |
| pylint                    | 376 ms                                                                                                         | 339 ms: 1.11x faster                                                                                       |
| nqueens                   | 97.2 ms                                                                                                        | 88.4 ms: 1.10x faster                                                                                      |
| gunicorn                  | 1.15 ms                                                                                                        | 1.04 ms: 1.10x faster                                                                                      |
| sympy_integrate           | 25.4 ms                                                                                                        | 23.2 ms: 1.10x faster                                                                                      |
| aiohttp                   | 1.17 ms                                                                                                        | 1.07 ms: 1.10x faster                                                                                      |
| deepcopy                  | 410 us                                                                                                         | 377 us: 1.09x faster                                                                                       |
| deepcopy_reduce           | 3.68 us                                                                                                        | 3.39 us: 1.09x faster                                                                                      |
| genshi_text               | 28.2 ms                                                                                                        | 25.9 ms: 1.09x faster                                                                                      |
| chaos                     | 64.4 ms                                                                                                        | 59.6 ms: 1.08x faster                                                                                      |
| typing_runtime_protocols  | 184 us                                                                                                         | 171 us: 1.08x faster                                                                                       |
| async_generators          | 389 ms                                                                                                         | 363 ms: 1.07x faster                                                                                       |
| python_startup_no_site    | 9.44 ms                                                                                                        | 8.85 ms: 1.07x faster                                                                                      |
| sympy_sum                 | 165 ms                                                                                                         | 155 ms: 1.07x faster                                                                                       |
| django_template           | 41.4 ms                                                                                                        | 39.0 ms: 1.06x faster                                                                                      |
| sympy_expand              | 532 ms                                                                                                         | 501 ms: 1.06x faster                                                                                       |
| sqlglot_normalize         | 127 ms                                                                                                         | 120 ms: 1.06x faster                                                                                       |
| sqlglot_optimize          | 62.9 ms                                                                                                        | 59.5 ms: 1.06x faster                                                                                      |
| async_tree_io             | 921 ms                                                                                                         | 873 ms: 1.05x faster                                                                                       |
| sympy_str                 | 310 ms                                                                                                         | 295 ms: 1.05x faster                                                                                       |
| flaskblogging             | 4.92 ms                                                                                                        | 4.68 ms: 1.05x faster                                                                                      |
| async_tree_memoization_tg | 441 ms                                                                                                         | 421 ms: 1.05x faster                                                                                       |
| regex_effbot              | 3.56 ms                                                                                                        | 3.40 ms: 1.05x faster                                                                                      |
| comprehensions            | 17.8 us                                                                                                        | 17.0 us: 1.05x faster                                                                                      |
| 2to3                      | 305 ms                                                                                                         | 291 ms: 1.05x faster                                                                                       |
| hexiom                    | 6.65 ms                                                                                                        | 6.35 ms: 1.05x faster                                                                                      |
| python_startup            | 13.8 ms                                                                                                        | 13.2 ms: 1.05x faster                                                                                      |
| dask                      | 408 ms                                                                                                         | 391 ms: 1.04x faster                                                                                       |
| async_tree_cpu_io_mixed   | 628 ms                                                                                                         | 604 ms: 1.04x faster                                                                                       |
| async_tree_none           | 380 ms                                                                                                         | 365 ms: 1.04x faster                                                                                       |
| thrift                    | 913 us                                                                                                         | 880 us: 1.04x faster                                                                                       |
| bench_thread_pool         | 941 us                                                                                                         | 908 us: 1.04x faster                                                                                       |
| mdp                       | 2.55 sec                                                                                                       | 2.46 sec: 1.04x faster                                                                                     |
| sqlglot_transpile         | 1.82 ms                                                                                                        | 1.76 ms: 1.03x faster                                                                                      |
| logging_simple            | 6.61 us                                                                                                        | 6.40 us: 1.03x faster                                                                                      |
| tornado_http              | 123 ms                                                                                                         | 119 ms: 1.03x faster                                                                                       |
| generators                | 34.3 ms                                                                                                        | 33.5 ms: 1.02x faster                                                                                      |
| pycparser                 | 1.25 sec                                                                                                       | 1.22 sec: 1.02x faster                                                                                     |
| sqlglot_parse             | 1.42 ms                                                                                                        | 1.39 ms: 1.02x faster                                                                                      |
| pathlib                   | 17.4 ms                                                                                                        | 17.1 ms: 1.02x faster                                                                                      |
| meteor_contest            | 130 ms                                                                                                         | 128 ms: 1.02x faster                                                                                       |
| coroutines                | 22.3 ms                                                                                                        | 22.0 ms: 1.01x faster                                                                                      |
| asyncio_tcp               | 382 ms                                                                                                         | 378 ms: 1.01x faster                                                                                       |
| chameleon                 | 7.48 ms                                                                                                        | 7.40 ms: 1.01x faster                                                                                      |
| unpickle_list             | 4.75 us                                                                                                        | 4.70 us: 1.01x faster                                                                                      |
| html5lib                  | 75.4 ms                                                                                                        | 74.7 ms: 1.01x faster                                                                                      |
| xml_etree_parse           | 145 ms                                                                                                         | 144 ms: 1.01x faster                                                                                       |
| pickle_pure_python        | 310 us                                                                                                         | 307 us: 1.01x faster                                                                                       |
| logging_format            | 7.17 us                                                                                                        | 7.11 us: 1.01x faster                                                                                      |
| scimark_monte_carlo       | 65.9 ms                                                                                                        | 65.5 ms: 1.01x faster                                                                                      |
| go                        | 166 ms                                                                                                         | 165 ms: 1.00x faster                                                                                       |
| bpe_tokeniser             | 5.13 sec                                                                                                       | 5.14 sec: 1.00x slower                                                                                     |
| deepcopy_memo             | 37.2 us                                                                                                        | 37.3 us: 1.00x slower                                                                                      |
| regex_dna                 | 248 ms                                                                                                         | 249 ms: 1.00x slower                                                                                       |
| asyncio_websockets        | 391 ms                                                                                                         | 395 ms: 1.01x slower                                                                                       |
| json                      | 5.30 ms                                                                                                        | 5.35 ms: 1.01x slower                                                                                      |
| json_dumps                | 10.7 ms                                                                                                        | 10.8 ms: 1.01x slower                                                                                      |
| pidigits                  | 250 ms                                                                                                         | 254 ms: 1.01x slower                                                                                       |
| dulwich_log               | 66.2 ms                                                                                                        | 67.3 ms: 1.02x slower                                                                                      |
| pprint_pformat            | 1.63 sec                                                                                                       | 1.66 sec: 1.02x slower                                                                                     |
| xml_etree_process         | 58.5 ms                                                                                                        | 59.7 ms: 1.02x slower                                                                                      |
| pickle_list               | 4.35 us                                                                                                        | 4.44 us: 1.02x slower                                                                                      |
| json_loads                | 24.4 us                                                                                                        | 25.0 us: 1.03x slower                                                                                      |
| regex_v8                  | 25.2 ms                                                                                                        | 26.0 ms: 1.03x slower                                                                                      |
| xml_etree_iterparse       | 99.3 ms                                                                                                        | 103 ms: 1.03x slower                                                                                       |
| pprint_safe_repr          | 792 ms                                                                                                         | 818 ms: 1.03x slower                                                                                       |
| coverage                  | 80.7 ms                                                                                                        | 83.5 ms: 1.03x slower                                                                                      |
| create_gc_cycles          | 1.94 ms                                                                                                        | 2.00 ms: 1.03x slower                                                                                      |
| regex_compile             | 139 ms                                                                                                         | 144 ms: 1.04x slower                                                                                       |
| xml_etree_generate        | 82.4 ms                                                                                                        | 85.7 ms: 1.04x slower                                                                                      |
| crypto_pyaes              | 70.6 ms                                                                                                        | 73.6 ms: 1.04x slower                                                                                      |
| telco                     | 8.05 ms                                                                                                        | 8.40 ms: 1.04x slower                                                                                      |
| gc_traversal              | 4.49 ms                                                                                                        | 4.69 ms: 1.04x slower                                                                                      |
| nbody                     | 82.9 ms                                                                                                        | 87.8 ms: 1.06x slower                                                                                      |
| unpickle_pure_python      | 211 us                                                                                                         | 224 us: 1.06x slower                                                                                       |
| pickle_dict               | 30.9 us                                                                                                        | 32.8 us: 1.06x slower                                                                                      |
| fannkuch                  | 331 ms                                                                                                         | 353 ms: 1.07x slower                                                                                       |
| scimark_fft               | 292 ms                                                                                                         | 312 ms: 1.07x slower                                                                                       |
| pyflate                   | 449 ms                                                                                                         | 482 ms: 1.07x slower                                                                                       |
| scimark_sparse_mat_mult   | 3.99 ms                                                                                                        | 4.28 ms: 1.07x slower                                                                                      |
| float                     | 74.2 ms                                                                                                        | 80.2 ms: 1.08x slower                                                                                      |
| mako                      | 9.10 ms                                                                                                        | 10.4 ms: 1.14x slower                                                                                      |
| richards                  | 46.5 ms                                                                                                        | 53.4 ms: 1.15x slower                                                                                      |
| tomli_loads               | 2.09 sec                                                                                                       | 2.40 sec: 1.15x slower                                                                                     |
| richards_super            | 52.8 ms                                                                                                        | 61.2 ms: 1.16x slower                                                                                      |
| spectral_norm             | 82.3 ms                                                                                                        | 97.3 ms: 1.18x slower                                                                                      |
| Geometric mean            | (ref)                                                                                                          | 1.02x faster                                                                                               |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, sqlite_synth, pickle, unpickle, async_tree_io_tg, async_tree_memoization, bench_mp_pool
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: docutils

# HPT report

- Reliability score: 97.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x