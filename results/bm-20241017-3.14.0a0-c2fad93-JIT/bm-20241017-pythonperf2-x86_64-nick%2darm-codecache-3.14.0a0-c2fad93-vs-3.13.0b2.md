# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.07x slower
- HPT reliability: 55.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 316 ms: 1.08x slower                                                 |
| docutils       | 2.98 sec                                                         | 3.22 sec: 1.08x slower                                               |
| html5lib       | 74.7 ms                                                          | 71.5 ms: 1.04x faster                                                |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                            | 1.03x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 365 ms                                                           | 322 ms: 1.13x faster                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 375 ms: 1.12x faster                                                 |
| async_tree_memoization     | 460 ms                                                           | 411 ms: 1.12x faster                                                 |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                 |
| async_tree_io_tg           | 900 ms                                                           | 825 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 564 ms: 1.07x faster                                                 |
| async_tree_io              | 873 ms                                                           | 837 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 557 ms: 1.03x faster                                                 |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 80.3 ms: 1.09x faster                                                |
| float          | 80.2 ms                                                          | 78.1 ms: 1.03x faster                                                |
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                            | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.01x faster                                                |
| regex_dna      | 249 ms                                                           | 247 ms: 1.01x faster                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.47 ms: 1.02x slower                                                |
| regex_compile  | 144 ms                                                           | 147 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                            | 1.00x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.18 sec: 1.10x faster                                               |
| pickle_dict          | 32.8 us                                                          | 30.2 us: 1.09x faster                                                |
| xml_etree_generate   | 85.7 ms                                                          | 79.4 ms: 1.08x faster                                                |
| xml_etree_process    | 59.7 ms                                                          | 56.6 ms: 1.05x faster                                                |
| json_loads           | 25.0 us                                                          | 23.9 us: 1.05x faster                                                |
| pickle_list          | 4.44 us                                                          | 4.25 us: 1.05x faster                                                |
| json_dumps           | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                                |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                                |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                 |
| unpickle_list        | 4.70 us                                                          | 4.75 us: 1.01x slower                                                |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                 |
| pickle_pure_python   | 307 us                                                           | 335 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                         |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.99 ms: 1.02x slower                                                |
| python_startup         | 13.2 ms                                                          | 14.9 ms: 1.13x slower                                                |
| Geometric mean         | (ref)                                                            | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                |
| django_template | 39.0 ms                                                          | 42.5 ms: 1.09x slower                                                |
| genshi_xml      | 58.1 ms                                                          | 64.8 ms: 1.12x slower                                                |
| genshi_text     | 25.9 ms                                                          | 28.9 ms: 1.12x slower                                                |
| Geometric mean  | (ref)                                                            | 1.05x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:----------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.1 us: 1.33x faster                                                |
| deepcopy                   | 377 us                                                           | 302 us: 1.25x faster                                                 |
| richards                   | 53.4 ms                                                          | 45.0 ms: 1.19x faster                                                |
| richards_super             | 61.2 ms                                                          | 53.3 ms: 1.15x faster                                                |
| deepcopy_reduce            | 3.39 us                                                          | 2.98 us: 1.14x faster                                                |
| async_tree_none            | 365 ms                                                           | 322 ms: 1.13x faster                                                 |
| mako                       | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                |
| scimark_sor                | 119 ms                                                           | 106 ms: 1.12x faster                                                 |
| scimark_fft                | 312 ms                                                           | 278 ms: 1.12x faster                                                 |
| async_tree_memoization_tg  | 421 ms                                                           | 375 ms: 1.12x faster                                                 |
| async_tree_memoization     | 460 ms                                                           | 411 ms: 1.12x faster                                                 |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.18 sec: 1.10x faster                                               |
| nbody                      | 87.8 ms                                                          | 80.3 ms: 1.09x faster                                                |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                |
| async_tree_io_tg           | 900 ms                                                           | 825 ms: 1.09x faster                                                 |
| go                         | 165 ms                                                           | 152 ms: 1.09x faster                                                 |
| pickle_dict                | 32.8 us                                                          | 30.2 us: 1.09x faster                                                |
| telco                      | 8.40 ms                                                          | 7.76 ms: 1.08x faster                                                |
| xml_etree_generate         | 85.7 ms                                                          | 79.4 ms: 1.08x faster                                                |
| spectral_norm              | 97.3 ms                                                          | 90.2 ms: 1.08x faster                                                |
| bpe_tokeniser              | 5.14 sec                                                         | 4.79 sec: 1.07x faster                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 564 ms: 1.07x faster                                                 |
| pyflate                    | 482 ms                                                           | 450 ms: 1.07x faster                                                 |
| logging_silent             | 96.3 ns                                                          | 90.2 ns: 1.07x faster                                                |
| coverage                   | 83.5 ms                                                          | 78.4 ms: 1.06x faster                                                |
| xml_etree_process          | 59.7 ms                                                          | 56.6 ms: 1.05x faster                                                |
| json_loads                 | 25.0 us                                                          | 23.9 us: 1.05x faster                                                |
| pickle_list                | 4.44 us                                                          | 4.25 us: 1.05x faster                                                |
| html5lib                   | 74.7 ms                                                          | 71.5 ms: 1.04x faster                                                |
| async_tree_io              | 873 ms                                                           | 837 ms: 1.04x faster                                                 |
| deltablue                  | 3.37 ms                                                          | 3.24 ms: 1.04x faster                                                |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.13 ms: 1.04x faster                                                |
| json                       | 5.35 ms                                                          | 5.17 ms: 1.03x faster                                                |
| crypto_pyaes               | 73.6 ms                                                          | 71.1 ms: 1.03x faster                                                |
| sqlite_synth               | 2.80 us                                                          | 2.71 us: 1.03x faster                                                |
| pprint_safe_repr           | 818 ms                                                           | 794 ms: 1.03x faster                                                 |
| asyncio_websockets         | 395 ms                                                           | 383 ms: 1.03x faster                                                 |
| json_dumps                 | 10.8 ms                                                          | 10.5 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 557 ms: 1.03x faster                                                 |
| pickle                     | 10.6 us                                                          | 10.3 us: 1.03x faster                                                |
| float                      | 80.2 ms                                                          | 78.1 ms: 1.03x faster                                                |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                |
| pprint_pformat             | 1.66 sec                                                         | 1.62 sec: 1.02x faster                                               |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                                 |
| dulwich_log                | 67.3 ms                                                          | 65.9 ms: 1.02x faster                                                |
| regex_v8                   | 26.0 ms                                                          | 25.6 ms: 1.01x faster                                                |
| regex_dna                  | 249 ms                                                           | 247 ms: 1.01x faster                                                 |
| pidigits                   | 254 ms                                                           | 252 ms: 1.01x faster                                                 |
| scimark_lu                 | 97.5 ms                                                          | 97.0 ms: 1.00x faster                                                |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                               |
| unpickle_list              | 4.70 us                                                          | 4.75 us: 1.01x slower                                                |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                 |
| python_startup_no_site     | 8.85 ms                                                          | 8.99 ms: 1.02x slower                                                |
| regex_effbot               | 3.40 ms                                                          | 3.47 ms: 1.02x slower                                                |
| regex_compile              | 144 ms                                                           | 147 ms: 1.02x slower                                                 |
| tornado_http               | 119 ms                                                           | 122 ms: 1.02x slower                                                 |
| logging_format             | 7.11 us                                                          | 7.28 us: 1.02x slower                                                |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.03x slower                                               |
| fannkuch                   | 353 ms                                                           | 367 ms: 1.04x slower                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.3 ms: 1.04x slower                                                |
| meteor_contest             | 128 ms                                                           | 134 ms: 1.04x slower                                                 |
| logging_simple             | 6.40 us                                                          | 6.71 us: 1.05x slower                                                |
| sympy_expand               | 501 ms                                                           | 526 ms: 1.05x slower                                                 |
| mdp                        | 2.46 sec                                                         | 2.62 sec: 1.06x slower                                               |
| async_generators           | 363 ms                                                           | 386 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 171 us                                                           | 181 us: 1.06x slower                                                 |
| bench_thread_pool          | 908 us                                                           | 968 us: 1.07x slower                                                 |
| sqlglot_parse              | 1.39 ms                                                          | 1.50 ms: 1.08x slower                                                |
| docutils                   | 2.98 sec                                                         | 3.22 sec: 1.08x slower                                               |
| 2to3                       | 291 ms                                                           | 316 ms: 1.08x slower                                                 |
| sympy_str                  | 295 ms                                                           | 320 ms: 1.09x slower                                                 |
| pickle_pure_python         | 307 us                                                           | 335 us: 1.09x slower                                                 |
| django_template            | 39.0 ms                                                          | 42.5 ms: 1.09x slower                                                |
| gc_traversal               | 4.69 ms                                                          | 5.17 ms: 1.10x slower                                                |
| genshi_xml                 | 58.1 ms                                                          | 64.8 ms: 1.12x slower                                                |
| genshi_text                | 25.9 ms                                                          | 28.9 ms: 1.12x slower                                                |
| sqlglot_transpile          | 1.76 ms                                                          | 1.97 ms: 1.12x slower                                                |
| sqlglot_normalize          | 120 ms                                                           | 135 ms: 1.12x slower                                                 |
| hexiom                     | 6.35 ms                                                          | 7.13 ms: 1.12x slower                                                |
| sympy_sum                  | 155 ms                                                           | 174 ms: 1.13x slower                                                 |
| python_startup             | 13.2 ms                                                          | 14.9 ms: 1.13x slower                                                |
| comprehensions             | 17.0 us                                                          | 19.4 us: 1.15x slower                                                |
| chaos                      | 59.6 ms                                                          | 68.4 ms: 1.15x slower                                                |
| nqueens                    | 88.4 ms                                                          | 102 ms: 1.16x slower                                                 |
| sqlglot_optimize           | 59.5 ms                                                          | 69.3 ms: 1.16x slower                                                |
| sympy_integrate            | 23.2 ms                                                          | 27.3 ms: 1.18x slower                                                |
| generators                 | 33.5 ms                                                          | 39.8 ms: 1.19x slower                                                |
| pylint                     | 339 ms                                                           | 418 ms: 1.23x slower                                                 |
| raytrace                   | 260 ms                                                           | 324 ms: 1.25x slower                                                 |
| create_gc_cycles           | 2.00 ms                                                          | 2.80 ms: 1.40x slower                                                |
| bench_mp_pool              | 4.91 ms                                                          | 2.97 sec: 605.37x slower                                             |
| Geometric mean             | (ref)                                                            | 1.07x slower                                                         |

Benchmark hidden because not significant (4): asyncio_tcp, xml_etree_iterparse, unpickle, thrift
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 55.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.20x