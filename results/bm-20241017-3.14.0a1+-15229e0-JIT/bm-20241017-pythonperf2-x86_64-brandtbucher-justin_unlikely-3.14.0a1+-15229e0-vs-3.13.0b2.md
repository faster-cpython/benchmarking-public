# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.08x slower
- HPT reliability: 56.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 317 ms: 1.09x slower                                                          |
| docutils       | 2.98 sec                                                         | 3.21 sec: 1.08x slower                                                        |
| html5lib       | 74.7 ms                                                          | 70.3 ms: 1.06x faster                                                         |
| tornado_http   | 119 ms                                                           | 124 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 421 ms                                                           | 373 ms: 1.13x faster                                                          |
| async_tree_memoization     | 460 ms                                                           | 408 ms: 1.13x faster                                                          |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 340 ms                                                           | 320 ms: 1.06x faster                                                          |
| async_tree_io              | 873 ms                                                           | 821 ms: 1.06x faster                                                          |
| async_tree_io_tg           | 900 ms                                                           | 857 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 576 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 559 ms: 1.02x faster                                                          |
| Geometric mean             | (ref)                                                            | 1.07x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 84.6 ms: 1.04x faster                                                         |
| float          | 80.2 ms                                                          | 78.7 ms: 1.02x faster                                                         |
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 231 ms: 1.08x faster                                                          |
| regex_v8       | 26.0 ms                                                          | 24.9 ms: 1.04x faster                                                         |
| regex_effbot   | 3.40 ms                                                          | 3.42 ms: 1.00x slower                                                         |
| regex_compile  | 144 ms                                                           | 153 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                        |
| unpickle             | 15.7 us                                                          | 14.8 us: 1.06x faster                                                         |
| xml_etree_generate   | 85.7 ms                                                          | 81.4 ms: 1.05x faster                                                         |
| xml_etree_process    | 59.7 ms                                                          | 56.9 ms: 1.05x faster                                                         |
| json_loads           | 25.0 us                                                          | 24.1 us: 1.04x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                          |
| unpickle_pure_python | 224 us                                                           | 223 us: 1.01x faster                                                          |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.00x faster                                                          |
| json_dumps           | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                         |
| pickle_list          | 4.44 us                                                          | 4.60 us: 1.04x slower                                                         |
| unpickle_list        | 4.70 us                                                          | 4.90 us: 1.04x slower                                                         |
| pickle_pure_python   | 307 us                                                           | 332 us: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                                         |
| python_startup         | 13.2 ms                                                          | 15.0 ms: 1.14x slower                                                         |
| Geometric mean         | (ref)                                                            | 1.08x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.57 ms: 1.08x faster                                                         |
| genshi_xml      | 58.1 ms                                                          | 63.0 ms: 1.09x slower                                                         |
| django_template | 39.0 ms                                                          | 42.7 ms: 1.09x slower                                                         |
| genshi_text     | 25.9 ms                                                          | 28.8 ms: 1.11x slower                                                         |
| Geometric mean  | (ref)                                                            | 1.05x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 29.7 us: 1.26x faster                                                         |
| richards_super             | 61.2 ms                                                          | 49.8 ms: 1.23x faster                                                         |
| richards                   | 53.4 ms                                                          | 44.5 ms: 1.20x faster                                                         |
| deepcopy                   | 377 us                                                           | 319 us: 1.18x faster                                                          |
| scimark_sor                | 119 ms                                                           | 104 ms: 1.14x faster                                                          |
| tomli_loads                | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 373 ms: 1.13x faster                                                          |
| async_tree_memoization     | 460 ms                                                           | 408 ms: 1.13x faster                                                          |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                          |
| deepcopy_reduce            | 3.39 us                                                          | 3.11 us: 1.09x faster                                                         |
| scimark_fft                | 312 ms                                                           | 288 ms: 1.08x faster                                                          |
| telco                      | 8.40 ms                                                          | 7.74 ms: 1.08x faster                                                         |
| mako                       | 10.4 ms                                                          | 9.57 ms: 1.08x faster                                                         |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                         |
| regex_dna                  | 249 ms                                                           | 231 ms: 1.08x faster                                                          |
| bpe_tokeniser              | 5.14 sec                                                         | 4.77 sec: 1.08x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 320 ms: 1.06x faster                                                          |
| async_tree_io              | 873 ms                                                           | 821 ms: 1.06x faster                                                          |
| json                       | 5.35 ms                                                          | 5.03 ms: 1.06x faster                                                         |
| unpickle                   | 15.7 us                                                          | 14.8 us: 1.06x faster                                                         |
| html5lib                   | 74.7 ms                                                          | 70.3 ms: 1.06x faster                                                         |
| go                         | 165 ms                                                           | 156 ms: 1.06x faster                                                          |
| logging_silent             | 96.3 ns                                                          | 91.4 ns: 1.05x faster                                                         |
| xml_etree_generate         | 85.7 ms                                                          | 81.4 ms: 1.05x faster                                                         |
| async_tree_io_tg           | 900 ms                                                           | 857 ms: 1.05x faster                                                          |
| xml_etree_process          | 59.7 ms                                                          | 56.9 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 576 ms: 1.05x faster                                                          |
| pyflate                    | 482 ms                                                           | 460 ms: 1.05x faster                                                          |
| coverage                   | 83.5 ms                                                          | 79.8 ms: 1.05x faster                                                         |
| regex_v8                   | 26.0 ms                                                          | 24.9 ms: 1.04x faster                                                         |
| spectral_norm              | 97.3 ms                                                          | 93.3 ms: 1.04x faster                                                         |
| json_loads                 | 25.0 us                                                          | 24.1 us: 1.04x faster                                                         |
| sqlite_synth               | 2.80 us                                                          | 2.69 us: 1.04x faster                                                         |
| nbody                      | 87.8 ms                                                          | 84.6 ms: 1.04x faster                                                         |
| pprint_safe_repr           | 818 ms                                                           | 788 ms: 1.04x faster                                                          |
| dulwich_log                | 67.3 ms                                                          | 65.0 ms: 1.03x faster                                                         |
| asyncio_websockets         | 395 ms                                                           | 383 ms: 1.03x faster                                                          |
| crypto_pyaes               | 73.6 ms                                                          | 71.4 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.66 sec                                                         | 1.61 sec: 1.03x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 94.7 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 559 ms: 1.02x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                          |
| deltablue                  | 3.37 ms                                                          | 3.30 ms: 1.02x faster                                                         |
| float                      | 80.2 ms                                                          | 78.7 ms: 1.02x faster                                                         |
| coroutines                 | 22.0 ms                                                          | 21.6 ms: 1.02x faster                                                         |
| logging_format             | 7.11 us                                                          | 7.04 us: 1.01x faster                                                         |
| pidigits                   | 254 ms                                                           | 252 ms: 1.01x faster                                                          |
| unpickle_pure_python       | 224 us                                                           | 223 us: 1.01x faster                                                          |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.00x faster                                                          |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.59 sec: 1.00x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.42 ms: 1.00x slower                                                         |
| python_startup_no_site     | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                                         |
| logging_simple             | 6.40 us                                                          | 6.53 us: 1.02x slower                                                         |
| thrift                     | 880 us                                                           | 898 us: 1.02x slower                                                          |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.41 ms: 1.03x slower                                                         |
| fannkuch                   | 353 ms                                                           | 364 ms: 1.03x slower                                                          |
| json_dumps                 | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                         |
| pickle_list                | 4.44 us                                                          | 4.60 us: 1.04x slower                                                         |
| tornado_http               | 119 ms                                                           | 124 ms: 1.04x slower                                                          |
| unpickle_list              | 4.70 us                                                          | 4.90 us: 1.04x slower                                                         |
| async_generators           | 363 ms                                                           | 380 ms: 1.05x slower                                                          |
| bench_thread_pool          | 908 us                                                           | 955 us: 1.05x slower                                                          |
| meteor_contest             | 128 ms                                                           | 135 ms: 1.05x slower                                                          |
| mdp                        | 2.46 sec                                                         | 2.62 sec: 1.06x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 69.7 ms: 1.06x slower                                                         |
| regex_compile              | 144 ms                                                           | 153 ms: 1.07x slower                                                          |
| pycparser                  | 1.22 sec                                                         | 1.30 sec: 1.07x slower                                                        |
| sympy_expand               | 501 ms                                                           | 535 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 171 us                                                           | 182 us: 1.07x slower                                                          |
| docutils                   | 2.98 sec                                                         | 3.21 sec: 1.08x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 332 us: 1.08x slower                                                          |
| genshi_xml                 | 58.1 ms                                                          | 63.0 ms: 1.09x slower                                                         |
| sqlglot_parse              | 1.39 ms                                                          | 1.51 ms: 1.09x slower                                                         |
| 2to3                       | 291 ms                                                           | 317 ms: 1.09x slower                                                          |
| chaos                      | 59.6 ms                                                          | 65.2 ms: 1.09x slower                                                         |
| sympy_str                  | 295 ms                                                           | 322 ms: 1.09x slower                                                          |
| django_template            | 39.0 ms                                                          | 42.7 ms: 1.09x slower                                                         |
| comprehensions             | 17.0 us                                                          | 18.6 us: 1.10x slower                                                         |
| sqlglot_normalize          | 120 ms                                                           | 133 ms: 1.11x slower                                                          |
| genshi_text                | 25.9 ms                                                          | 28.8 ms: 1.11x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                          | 1.98 ms: 1.12x slower                                                         |
| hexiom                     | 6.35 ms                                                          | 7.18 ms: 1.13x slower                                                         |
| python_startup             | 13.2 ms                                                          | 15.0 ms: 1.14x slower                                                         |
| sympy_sum                  | 155 ms                                                           | 176 ms: 1.14x slower                                                          |
| gc_traversal               | 4.69 ms                                                          | 5.35 ms: 1.14x slower                                                         |
| nqueens                    | 88.4 ms                                                          | 101 ms: 1.15x slower                                                          |
| raytrace                   | 260 ms                                                           | 299 ms: 1.15x slower                                                          |
| generators                 | 33.5 ms                                                          | 38.9 ms: 1.16x slower                                                         |
| sqlglot_optimize           | 59.5 ms                                                          | 69.9 ms: 1.17x slower                                                         |
| sympy_integrate            | 23.2 ms                                                          | 27.6 ms: 1.19x slower                                                         |
| pylint                     | 339 ms                                                           | 425 ms: 1.25x slower                                                          |
| create_gc_cycles           | 2.00 ms                                                          | 2.92 ms: 1.46x slower                                                         |
| bench_mp_pool              | 4.91 ms                                                          | 3.14 sec: 640.00x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.08x slower                                                                  |

Benchmark hidden because not significant (3): asyncio_tcp, pickle, pickle_dict
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf2-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 56.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x