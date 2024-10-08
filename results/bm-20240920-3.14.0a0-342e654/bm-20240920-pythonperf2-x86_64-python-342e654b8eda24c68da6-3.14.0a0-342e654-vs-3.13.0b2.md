# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 282 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                      |
| html5lib       | 74.7 ms                                                          | 72.4 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 790 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 807 ms: 1.08x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 570 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.06x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.2 ms: 1.03x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| nbody          | 87.8 ms                                                          | 91.6 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                                       |
| regex_dna      | 249 ms                                                           | 245 ms: 1.02x faster                                                        |
| regex_compile  | 144 ms                                                           | 142 ms: 1.02x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.61 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.3 us: 1.08x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                                       |
| pickle               | 10.6 us                                                          | 10.2 us: 1.04x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.28 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| xml_etree_parse      | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| json_loads           | 25.0 us                                                          | 24.6 us: 1.02x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 84.9 ms: 1.01x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 59.4 ms: 1.01x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 229 us: 1.02x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 321 us: 1.04x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.63 sec: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                                       |
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 56.4 ms: 1.03x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.7 ms: 1.01x faster                                                       |
| django_template | 39.0 ms                                                          | 39.5 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 284 us: 1.33x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.3 us: 1.27x faster                                                       |
| go                         | 165 ms                                                           | 139 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.86 us: 1.19x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 790 ms: 1.14x faster                                                        |
| generators                 | 33.5 ms                                                          | 29.6 ms: 1.13x faster                                                       |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                       |
| pickle_dict                | 32.8 us                                                          | 30.3 us: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 807 ms: 1.08x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                                        |
| richards_super             | 61.2 ms                                                          | 57.0 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 570 ms: 1.06x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 857 us: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.06x faster                                                        |
| coverage                   | 83.5 ms                                                          | 79.6 ms: 1.05x faster                                                       |
| richards                   | 53.4 ms                                                          | 50.9 ms: 1.05x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.49 ms: 1.04x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.1 us: 1.04x faster                                                       |
| pickle                     | 10.6 us                                                          | 10.2 us: 1.04x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.94 sec: 1.04x faster                                                      |
| pickle_list                | 4.44 us                                                          | 4.28 us: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.12 ms: 1.04x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 116 ms: 1.03x faster                                                        |
| thrift                     | 880 us                                                           | 851 us: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                           | 282 ms: 1.03x faster                                                        |
| regex_v8                   | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 72.4 ms: 1.03x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.16 ms: 1.03x faster                                                       |
| genshi_xml                 | 58.1 ms                                                          | 56.4 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 57.9 ms: 1.03x faster                                                       |
| docutils                   | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                      |
| float                      | 80.2 ms                                                          | 78.2 ms: 1.03x faster                                                       |
| scimark_fft                | 312 ms                                                           | 305 ms: 1.02x faster                                                        |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| regex_dna                  | 249 ms                                                           | 245 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 802 ms: 1.02x faster                                                        |
| json_loads                 | 25.0 us                                                          | 24.6 us: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.98 us: 1.02x faster                                                       |
| regex_compile              | 144 ms                                                           | 142 ms: 1.02x faster                                                        |
| json                       | 5.35 ms                                                          | 5.26 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 372 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                      |
| dulwich_log                | 67.3 ms                                                          | 66.4 ms: 1.01x faster                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                        |
| async_generators           | 363 ms                                                           | 359 ms: 1.01x faster                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.77 us: 1.01x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.9 ms: 1.01x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.7 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 96.7 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 73.2 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.01x faster                                                      |
| xml_etree_process          | 59.7 ms                                                          | 59.4 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| comprehensions             | 17.0 us                                                          | 17.0 us: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 89.1 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| scimark_sor                | 119 ms                                                           | 120 ms: 1.01x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.42 ms: 1.01x slower                                                       |
| django_template            | 39.0 ms                                                          | 39.5 ms: 1.01x slower                                                       |
| scimark_lu                 | 97.5 ms                                                          | 99.0 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 224 us                                                           | 229 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| fannkuch                   | 353 ms                                                           | 361 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.1 ms: 1.02x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                                      |
| typing_runtime_protocols   | 171 us                                                           | 176 us: 1.03x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 99.7 ns: 1.04x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 321 us: 1.04x slower                                                        |
| nbody                      | 87.8 ms                                                          | 91.6 ms: 1.04x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.61 ms: 1.06x slower                                                       |
| chaos                      | 59.6 ms                                                          | 63.4 ms: 1.06x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.63 sec: 1.09x slower                                                      |
| raytrace                   | 260 ms                                                           | 286 ms: 1.10x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (13): bench_mp_pool, create_gc_cycles, telco, logging_simple, unpickle_list, pycparser, sympy_expand, coroutines, mako, pyflate, sympy_str, asyncio_websockets, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x