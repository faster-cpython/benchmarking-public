# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.01x slower
- HPT reliability: 89.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                      | 282 ms: 1.00x slower                                               |
| docutils       | 2.90 sec                                                                    | 2.91 sec: 1.00x slower                                             |
| html5lib       | 71.5 ms                                                                     | 70.9 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 795 ms                                                                      | 774 ms: 1.03x faster                                               |
| asyncio_websockets         | 396 ms                                                                      | 391 ms: 1.01x faster                                               |
| async_tree_memoization     | 400 ms                                                                      | 397 ms: 1.01x faster                                               |
| asyncio_tcp_ssl            | 1.57 sec                                                                    | 1.58 sec: 1.00x slower                                             |
| coroutines                 | 21.4 ms                                                                     | 21.9 ms: 1.02x slower                                              |
| async_tree_cpu_io_mixed_tg | 545 ms                                                                      | 559 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                       |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, asyncio_tcp, async_generators, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.3 ms                                                                     | 79.6 ms: 1.02x slower                                              |
| nbody          | 87.2 ms                                                                     | 89.1 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.64 ms                                                                     | 3.51 ms: 1.04x faster                                              |
| regex_v8       | 25.5 ms                                                                     | 25.0 ms: 1.02x faster                                              |
| regex_dna      | 241 ms                                                                      | 237 ms: 1.02x faster                                               |
| regex_compile  | 140 ms                                                                      | 139 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_list          | 4.50 us                                                                     | 4.18 us: 1.08x faster                                              |
| pickle_dict          | 32.4 us                                                                     | 30.3 us: 1.07x faster                                              |
| pickle               | 10.5 us                                                                     | 10.3 us: 1.02x faster                                              |
| unpickle_pure_python | 220 us                                                                      | 216 us: 1.02x faster                                               |
| json_loads           | 25.1 us                                                                     | 24.8 us: 1.01x faster                                              |
| xml_etree_process    | 59.9 ms                                                                     | 59.2 ms: 1.01x faster                                              |
| xml_etree_generate   | 85.6 ms                                                                     | 84.8 ms: 1.01x faster                                              |
| json_dumps           | 10.8 ms                                                                     | 10.9 ms: 1.01x slower                                              |
| xml_etree_parse      | 143 ms                                                                      | 145 ms: 1.02x slower                                               |
| pickle_pure_python   | 317 us                                                                      | 323 us: 1.02x slower                                               |
| tomli_loads          | 2.53 sec                                                                    | 2.58 sec: 1.02x slower                                             |
| unpickle_list        | 4.56 us                                                                     | 4.81 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                       |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                                     | 13.4 ms: 1.00x slower                                              |
| python_startup_no_site | 8.94 ms                                                                     | 8.98 ms: 1.00x slower                                              |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 24.9 ms                                                                     | 24.8 ms: 1.01x faster                                              |
| genshi_xml      | 54.6 ms                                                                     | 55.4 ms: 1.01x slower                                              |
| mako            | 10.4 ms                                                                     | 10.6 ms: 1.02x slower                                              |
| django_template | 38.3 ms                                                                     | 39.6 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_list                | 4.50 us                                                                     | 4.18 us: 1.08x faster                                              |
| pickle_dict                | 32.4 us                                                                     | 30.3 us: 1.07x faster                                              |
| bench_mp_pool              | 4.85 ms                                                                     | 4.63 ms: 1.05x faster                                              |
| regex_effbot               | 3.64 ms                                                                     | 3.51 ms: 1.04x faster                                              |
| async_tree_io_tg           | 795 ms                                                                      | 774 ms: 1.03x faster                                               |
| pickle                     | 10.5 us                                                                     | 10.3 us: 1.02x faster                                              |
| regex_v8                   | 25.5 ms                                                                     | 25.0 ms: 1.02x faster                                              |
| unpickle_pure_python       | 220 us                                                                      | 216 us: 1.02x faster                                               |
| regex_dna                  | 241 ms                                                                      | 237 ms: 1.02x faster                                               |
| generators                 | 29.3 ms                                                                     | 28.8 ms: 1.02x faster                                              |
| pyflate                    | 492 ms                                                                      | 483 ms: 1.02x faster                                               |
| typing_runtime_protocols   | 175 us                                                                      | 172 us: 1.02x faster                                               |
| richards_super             | 56.5 ms                                                                     | 55.8 ms: 1.01x faster                                              |
| json_loads                 | 25.1 us                                                                     | 24.8 us: 1.01x faster                                              |
| xml_etree_process          | 59.9 ms                                                                     | 59.2 ms: 1.01x faster                                              |
| dulwich_log                | 67.3 ms                                                                     | 66.5 ms: 1.01x faster                                              |
| asyncio_websockets         | 396 ms                                                                      | 391 ms: 1.01x faster                                               |
| xml_etree_generate         | 85.6 ms                                                                     | 84.8 ms: 1.01x faster                                              |
| regex_compile              | 140 ms                                                                      | 139 ms: 1.01x faster                                               |
| crypto_pyaes               | 73.8 ms                                                                     | 73.2 ms: 1.01x faster                                              |
| html5lib                   | 71.5 ms                                                                     | 70.9 ms: 1.01x faster                                              |
| async_tree_memoization     | 400 ms                                                                      | 397 ms: 1.01x faster                                               |
| sympy_expand               | 500 ms                                                                      | 497 ms: 1.01x faster                                               |
| genshi_text                | 24.9 ms                                                                     | 24.8 ms: 1.01x faster                                              |
| bpe_tokeniser              | 4.97 sec                                                                    | 4.94 sec: 1.01x faster                                             |
| richards                   | 50.3 ms                                                                     | 50.0 ms: 1.00x faster                                              |
| deepcopy_memo              | 30.2 us                                                                     | 30.1 us: 1.00x faster                                              |
| meteor_contest             | 127 ms                                                                      | 127 ms: 1.00x slower                                               |
| sqlglot_optimize           | 59.0 ms                                                                     | 59.1 ms: 1.00x slower                                              |
| asyncio_tcp_ssl            | 1.57 sec                                                                    | 1.58 sec: 1.00x slower                                             |
| mdp                        | 2.50 sec                                                                    | 2.51 sec: 1.00x slower                                             |
| docutils                   | 2.90 sec                                                                    | 2.91 sec: 1.00x slower                                             |
| python_startup             | 13.3 ms                                                                     | 13.4 ms: 1.00x slower                                              |
| 2to3                       | 281 ms                                                                      | 282 ms: 1.00x slower                                               |
| sympy_integrate            | 23.0 ms                                                                     | 23.1 ms: 1.00x slower                                              |
| go                         | 134 ms                                                                      | 135 ms: 1.00x slower                                               |
| python_startup_no_site     | 8.94 ms                                                                     | 8.98 ms: 1.00x slower                                              |
| sqlite_synth               | 2.73 us                                                                     | 2.75 us: 1.01x slower                                              |
| raytrace                   | 272 ms                                                                      | 275 ms: 1.01x slower                                               |
| hexiom                     | 6.21 ms                                                                     | 6.26 ms: 1.01x slower                                              |
| pprint_pformat             | 1.66 sec                                                                    | 1.68 sec: 1.01x slower                                             |
| logging_silent             | 99.3 ns                                                                     | 100 ns: 1.01x slower                                               |
| json_dumps                 | 10.8 ms                                                                     | 10.9 ms: 1.01x slower                                              |
| spectral_norm              | 96.6 ms                                                                     | 97.6 ms: 1.01x slower                                              |
| sqlglot_normalize          | 118 ms                                                                      | 119 ms: 1.01x slower                                               |
| deltablue                  | 3.38 ms                                                                     | 3.42 ms: 1.01x slower                                              |
| sqlglot_parse              | 1.41 ms                                                                     | 1.43 ms: 1.01x slower                                              |
| genshi_xml                 | 54.6 ms                                                                     | 55.4 ms: 1.01x slower                                              |
| telco                      | 8.33 ms                                                                     | 8.45 ms: 1.01x slower                                              |
| pycparser                  | 1.21 sec                                                                    | 1.23 sec: 1.02x slower                                             |
| xml_etree_parse            | 143 ms                                                                      | 145 ms: 1.02x slower                                               |
| sqlglot_transpile          | 1.79 ms                                                                     | 1.81 ms: 1.02x slower                                              |
| deepcopy                   | 286 us                                                                      | 291 us: 1.02x slower                                               |
| float                      | 78.3 ms                                                                     | 79.6 ms: 1.02x slower                                              |
| pickle_pure_python         | 317 us                                                                      | 323 us: 1.02x slower                                               |
| pathlib                    | 15.6 ms                                                                     | 15.8 ms: 1.02x slower                                              |
| thrift                     | 859 us                                                                      | 875 us: 1.02x slower                                               |
| tomli_loads                | 2.53 sec                                                                    | 2.58 sec: 1.02x slower                                             |
| mako                       | 10.4 ms                                                                     | 10.6 ms: 1.02x slower                                              |
| nbody                      | 87.2 ms                                                                     | 89.1 ms: 1.02x slower                                              |
| coroutines                 | 21.4 ms                                                                     | 21.9 ms: 1.02x slower                                              |
| scimark_fft                | 300 ms                                                                      | 307 ms: 1.02x slower                                               |
| deepcopy_reduce            | 2.90 us                                                                     | 2.97 us: 1.02x slower                                              |
| fannkuch                   | 356 ms                                                                      | 365 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 545 ms                                                                      | 559 ms: 1.03x slower                                               |
| scimark_sparse_mat_mult    | 4.29 ms                                                                     | 4.40 ms: 1.03x slower                                              |
| logging_simple             | 6.37 us                                                                     | 6.58 us: 1.03x slower                                              |
| nqueens                    | 88.5 ms                                                                     | 91.4 ms: 1.03x slower                                              |
| bench_thread_pool          | 865 us                                                                      | 894 us: 1.03x slower                                               |
| django_template            | 38.3 ms                                                                     | 39.6 ms: 1.04x slower                                              |
| create_gc_cycles           | 1.92 ms                                                                     | 1.99 ms: 1.04x slower                                              |
| scimark_lu                 | 95.7 ms                                                                     | 99.2 ms: 1.04x slower                                              |
| coverage                   | 82.8 ms                                                                     | 86.1 ms: 1.04x slower                                              |
| logging_format             | 6.87 us                                                                     | 7.15 us: 1.04x slower                                              |
| comprehensions             | 17.0 us                                                                     | 17.7 us: 1.04x slower                                              |
| unpickle_list              | 4.56 us                                                                     | 4.81 us: 1.05x slower                                              |
| gc_traversal               | 4.45 ms                                                                     | 4.70 ms: 1.06x slower                                              |
| scimark_sor                | 117 ms                                                                      | 129 ms: 1.10x slower                                               |
| unpack_sequence            | 48.7 ns                                                                     | 55.2 ns: 1.13x slower                                              |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (18): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, xml_etree_iterparse, chaos, async_tree_memoization_tg, asyncio_tcp, json, sympy_sum, pprint_safe_repr, tornado_http, pidigits, unpickle, sympy_str, async_generators, pylint, scimark_monte_carlo, async_tree_io

# HPT report

- Reliability score: 89.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x