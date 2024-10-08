# Results vs. base

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.02x slower
- HPT reliability: 97.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                                                                     | 305 ms: 1.05x slower                                                                                           |
| chameleon      | 7.40 ms                                                                                                    | 7.48 ms: 1.01x slower                                                                                          |
| html5lib       | 74.7 ms                                                                                                    | 75.4 ms: 1.01x slower                                                                                          |
| tornado_http   | 119 ms                                                                                                     | 123 ms: 1.03x slower                                                                                           |
| Geometric mean | (ref)                                                                                                      | 1.02x slower                                                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| async_tree_none           | 365 ms                                                                                                     | 380 ms: 1.04x slower                                                                                           |
| async_tree_cpu_io_mixed   | 604 ms                                                                                                     | 628 ms: 1.04x slower                                                                                           |
| async_tree_memoization_tg | 421 ms                                                                                                     | 441 ms: 1.05x slower                                                                                           |
| async_tree_io             | 873 ms                                                                                                     | 921 ms: 1.05x slower                                                                                           |
| Geometric mean            | (ref)                                                                                                      | 1.02x slower                                                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                                                                    | 74.2 ms: 1.08x faster                                                                                          |
| nbody          | 87.8 ms                                                                                                    | 82.9 ms: 1.06x faster                                                                                          |
| pidigits       | 254 ms                                                                                                     | 250 ms: 1.01x faster                                                                                           |
| Geometric mean | (ref)                                                                                                      | 1.05x faster                                                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                                                                     | 139 ms: 1.04x faster                                                                                           |
| regex_v8       | 26.0 ms                                                                                                    | 25.2 ms: 1.03x faster                                                                                          |
| regex_dna      | 249 ms                                                                                                     | 248 ms: 1.00x faster                                                                                           |
| regex_effbot   | 3.40 ms                                                                                                    | 3.56 ms: 1.05x slower                                                                                          |
| Geometric mean | (ref)                                                                                                      | 1.01x faster                                                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                                                                   | 2.09 sec: 1.15x faster                                                                                         |
| pickle_dict          | 32.8 us                                                                                                    | 30.9 us: 1.06x faster                                                                                          |
| unpickle_pure_python | 224 us                                                                                                     | 211 us: 1.06x faster                                                                                           |
| xml_etree_generate   | 85.7 ms                                                                                                    | 82.4 ms: 1.04x faster                                                                                          |
| xml_etree_iterparse  | 103 ms                                                                                                     | 99.3 ms: 1.03x faster                                                                                          |
| json_loads           | 25.0 us                                                                                                    | 24.4 us: 1.03x faster                                                                                          |
| pickle_list          | 4.44 us                                                                                                    | 4.35 us: 1.02x faster                                                                                          |
| xml_etree_process    | 59.7 ms                                                                                                    | 58.5 ms: 1.02x faster                                                                                          |
| json_dumps           | 10.8 ms                                                                                                    | 10.7 ms: 1.01x faster                                                                                          |
| pickle_pure_python   | 307 us                                                                                                     | 310 us: 1.01x slower                                                                                           |
| xml_etree_parse      | 144 ms                                                                                                     | 145 ms: 1.01x slower                                                                                           |
| unpickle_list        | 4.70 us                                                                                                    | 4.75 us: 1.01x slower                                                                                          |
| Geometric mean       | (ref)                                                                                                      | 1.03x faster                                                                                                   |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                                                    | 13.8 ms: 1.05x slower                                                                                          |
| python_startup_no_site | 8.85 ms                                                                                                    | 9.44 ms: 1.07x slower                                                                                          |
| Geometric mean         | (ref)                                                                                                      | 1.06x slower                                                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                                                                    | 9.10 ms: 1.14x faster                                                                                          |
| django_template | 39.0 ms                                                                                                    | 41.4 ms: 1.06x slower                                                                                          |
| genshi_text     | 25.9 ms                                                                                                    | 28.2 ms: 1.09x slower                                                                                          |
| genshi_xml      | 58.1 ms                                                                                                    | 65.3 ms: 1.13x slower                                                                                          |
| Geometric mean  | (ref)                                                                                                      | 1.03x slower                                                                                                   |

All benchmarks:
===============

| Benchmark                 | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| spectral_norm             | 97.3 ms                                                                                                    | 82.3 ms: 1.18x faster                                                                                          |
| richards_super            | 61.2 ms                                                                                                    | 52.8 ms: 1.16x faster                                                                                          |
| tomli_loads               | 2.40 sec                                                                                                   | 2.09 sec: 1.15x faster                                                                                         |
| richards                  | 53.4 ms                                                                                                    | 46.5 ms: 1.15x faster                                                                                          |
| mako                      | 10.4 ms                                                                                                    | 9.10 ms: 1.14x faster                                                                                          |
| float                     | 80.2 ms                                                                                                    | 74.2 ms: 1.08x faster                                                                                          |
| scimark_sparse_mat_mult   | 4.28 ms                                                                                                    | 3.99 ms: 1.07x faster                                                                                          |
| pyflate                   | 482 ms                                                                                                     | 449 ms: 1.07x faster                                                                                           |
| scimark_fft               | 312 ms                                                                                                     | 292 ms: 1.07x faster                                                                                           |
| fannkuch                  | 353 ms                                                                                                     | 331 ms: 1.07x faster                                                                                           |
| pickle_dict               | 32.8 us                                                                                                    | 30.9 us: 1.06x faster                                                                                          |
| unpickle_pure_python      | 224 us                                                                                                     | 211 us: 1.06x faster                                                                                           |
| nbody                     | 87.8 ms                                                                                                    | 82.9 ms: 1.06x faster                                                                                          |
| gc_traversal              | 4.69 ms                                                                                                    | 4.49 ms: 1.04x faster                                                                                          |
| telco                     | 8.40 ms                                                                                                    | 8.05 ms: 1.04x faster                                                                                          |
| crypto_pyaes              | 73.6 ms                                                                                                    | 70.6 ms: 1.04x faster                                                                                          |
| xml_etree_generate        | 85.7 ms                                                                                                    | 82.4 ms: 1.04x faster                                                                                          |
| regex_compile             | 144 ms                                                                                                     | 139 ms: 1.04x faster                                                                                           |
| create_gc_cycles          | 2.00 ms                                                                                                    | 1.94 ms: 1.03x faster                                                                                          |
| coverage                  | 83.5 ms                                                                                                    | 80.7 ms: 1.03x faster                                                                                          |
| pprint_safe_repr          | 818 ms                                                                                                     | 792 ms: 1.03x faster                                                                                           |
| xml_etree_iterparse       | 103 ms                                                                                                     | 99.3 ms: 1.03x faster                                                                                          |
| regex_v8                  | 26.0 ms                                                                                                    | 25.2 ms: 1.03x faster                                                                                          |
| json_loads                | 25.0 us                                                                                                    | 24.4 us: 1.03x faster                                                                                          |
| pickle_list               | 4.44 us                                                                                                    | 4.35 us: 1.02x faster                                                                                          |
| xml_etree_process         | 59.7 ms                                                                                                    | 58.5 ms: 1.02x faster                                                                                          |
| pprint_pformat            | 1.66 sec                                                                                                   | 1.63 sec: 1.02x faster                                                                                         |
| dulwich_log               | 67.3 ms                                                                                                    | 66.2 ms: 1.02x faster                                                                                          |
| pidigits                  | 254 ms                                                                                                     | 250 ms: 1.01x faster                                                                                           |
| json_dumps                | 10.8 ms                                                                                                    | 10.7 ms: 1.01x faster                                                                                          |
| json                      | 5.35 ms                                                                                                    | 5.30 ms: 1.01x faster                                                                                          |
| asyncio_websockets        | 395 ms                                                                                                     | 391 ms: 1.01x faster                                                                                           |
| regex_dna                 | 249 ms                                                                                                     | 248 ms: 1.00x faster                                                                                           |
| deepcopy_memo             | 37.3 us                                                                                                    | 37.2 us: 1.00x faster                                                                                          |
| bpe_tokeniser             | 5.14 sec                                                                                                   | 5.13 sec: 1.00x faster                                                                                         |
| go                        | 165 ms                                                                                                     | 166 ms: 1.00x slower                                                                                           |
| scimark_monte_carlo       | 65.5 ms                                                                                                    | 65.9 ms: 1.01x slower                                                                                          |
| logging_format            | 7.11 us                                                                                                    | 7.17 us: 1.01x slower                                                                                          |
| pickle_pure_python        | 307 us                                                                                                     | 310 us: 1.01x slower                                                                                           |
| xml_etree_parse           | 144 ms                                                                                                     | 145 ms: 1.01x slower                                                                                           |
| html5lib                  | 74.7 ms                                                                                                    | 75.4 ms: 1.01x slower                                                                                          |
| unpickle_list             | 4.70 us                                                                                                    | 4.75 us: 1.01x slower                                                                                          |
| chameleon                 | 7.40 ms                                                                                                    | 7.48 ms: 1.01x slower                                                                                          |
| asyncio_tcp               | 378 ms                                                                                                     | 382 ms: 1.01x slower                                                                                           |
| coroutines                | 22.0 ms                                                                                                    | 22.3 ms: 1.01x slower                                                                                          |
| meteor_contest            | 128 ms                                                                                                     | 130 ms: 1.02x slower                                                                                           |
| pathlib                   | 17.1 ms                                                                                                    | 17.4 ms: 1.02x slower                                                                                          |
| sqlglot_parse             | 1.39 ms                                                                                                    | 1.42 ms: 1.02x slower                                                                                          |
| pycparser                 | 1.22 sec                                                                                                   | 1.25 sec: 1.02x slower                                                                                         |
| generators                | 33.5 ms                                                                                                    | 34.3 ms: 1.02x slower                                                                                          |
| tornado_http              | 119 ms                                                                                                     | 123 ms: 1.03x slower                                                                                           |
| logging_simple            | 6.40 us                                                                                                    | 6.61 us: 1.03x slower                                                                                          |
| sqlglot_transpile         | 1.76 ms                                                                                                    | 1.82 ms: 1.03x slower                                                                                          |
| mdp                       | 2.46 sec                                                                                                   | 2.55 sec: 1.04x slower                                                                                         |
| bench_thread_pool         | 908 us                                                                                                     | 941 us: 1.04x slower                                                                                           |
| thrift                    | 880 us                                                                                                     | 913 us: 1.04x slower                                                                                           |
| async_tree_none           | 365 ms                                                                                                     | 380 ms: 1.04x slower                                                                                           |
| async_tree_cpu_io_mixed   | 604 ms                                                                                                     | 628 ms: 1.04x slower                                                                                           |
| dask                      | 391 ms                                                                                                     | 408 ms: 1.04x slower                                                                                           |
| python_startup            | 13.2 ms                                                                                                    | 13.8 ms: 1.05x slower                                                                                          |
| hexiom                    | 6.35 ms                                                                                                    | 6.65 ms: 1.05x slower                                                                                          |
| 2to3                      | 291 ms                                                                                                     | 305 ms: 1.05x slower                                                                                           |
| comprehensions            | 17.0 us                                                                                                    | 17.8 us: 1.05x slower                                                                                          |
| regex_effbot              | 3.40 ms                                                                                                    | 3.56 ms: 1.05x slower                                                                                          |
| async_tree_memoization_tg | 421 ms                                                                                                     | 441 ms: 1.05x slower                                                                                           |
| flaskblogging             | 4.68 ms                                                                                                    | 4.92 ms: 1.05x slower                                                                                          |
| sympy_str                 | 295 ms                                                                                                     | 310 ms: 1.05x slower                                                                                           |
| async_tree_io             | 873 ms                                                                                                     | 921 ms: 1.05x slower                                                                                           |
| sqlglot_optimize          | 59.5 ms                                                                                                    | 62.9 ms: 1.06x slower                                                                                          |
| sqlglot_normalize         | 120 ms                                                                                                     | 127 ms: 1.06x slower                                                                                           |
| sympy_expand              | 501 ms                                                                                                     | 532 ms: 1.06x slower                                                                                           |
| django_template           | 39.0 ms                                                                                                    | 41.4 ms: 1.06x slower                                                                                          |
| sympy_sum                 | 155 ms                                                                                                     | 165 ms: 1.07x slower                                                                                           |
| python_startup_no_site    | 8.85 ms                                                                                                    | 9.44 ms: 1.07x slower                                                                                          |
| async_generators          | 363 ms                                                                                                     | 389 ms: 1.07x slower                                                                                           |
| typing_runtime_protocols  | 171 us                                                                                                     | 184 us: 1.08x slower                                                                                           |
| chaos                     | 59.6 ms                                                                                                    | 64.4 ms: 1.08x slower                                                                                          |
| genshi_text               | 25.9 ms                                                                                                    | 28.2 ms: 1.09x slower                                                                                          |
| deepcopy_reduce           | 3.39 us                                                                                                    | 3.68 us: 1.09x slower                                                                                          |
| deepcopy                  | 377 us                                                                                                     | 410 us: 1.09x slower                                                                                           |
| aiohttp                   | 1.07 ms                                                                                                    | 1.17 ms: 1.10x slower                                                                                          |
| sympy_integrate           | 23.2 ms                                                                                                    | 25.4 ms: 1.10x slower                                                                                          |
| gunicorn                  | 1.04 ms                                                                                                    | 1.15 ms: 1.10x slower                                                                                          |
| nqueens                   | 88.4 ms                                                                                                    | 97.2 ms: 1.10x slower                                                                                          |
| pylint                    | 339 ms                                                                                                     | 376 ms: 1.11x slower                                                                                           |
| mypy2                     | 764 ms                                                                                                     | 852 ms: 1.11x slower                                                                                           |
| genshi_xml                | 58.1 ms                                                                                                    | 65.3 ms: 1.13x slower                                                                                          |
| deltablue                 | 3.37 ms                                                                                                    | 3.81 ms: 1.13x slower                                                                                          |
| raytrace                  | 260 ms                                                                                                     | 297 ms: 1.14x slower                                                                                           |
| scimark_lu                | 97.5 ms                                                                                                    | 114 ms: 1.17x slower                                                                                           |
| scimark_sor               | 119 ms                                                                                                     | 144 ms: 1.21x slower                                                                                           |
| logging_silent            | 96.3 ns                                                                                                    | 123 ns: 1.28x slower                                                                                           |
| Geometric mean            | (ref)                                                                                                      | 1.02x slower                                                                                                   |

Benchmark hidden because not significant (9): bench_mp_pool, async_tree_memoization, async_tree_io_tg, unpickle, pickle, sqlite_synth, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_none_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: docutils

# HPT report

- Reliability score: 97.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x