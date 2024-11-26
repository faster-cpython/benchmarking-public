# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-amd64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.003x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                    |
| html5lib       | 38.9 ms                                                     | 40.0 ms: 1.03x slower                                                     |
| tornado_http   | 93.0 ms                                                     | 83.5 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x faster                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                      |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 261 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 396 ms: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                      |
| async_tree_io              | 521 ms                                                      | 571 ms: 1.09x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                                      |
| float          | 49.9 ms                                                     | 54.2 ms: 1.08x slower                                                     |
| nbody          | 68.4 ms                                                     | 82.1 ms: 1.20x slower                                                     |
| Geometric mean | (ref)                                                       | 1.10x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.4 ms: 1.49x faster                                                     |
| regex_effbot   | 1.58 ms                                                     | 1.54 ms: 1.02x faster                                                     |
| regex_dna      | 115 ms                                                      | 114 ms: 1.02x faster                                                      |
| regex_compile  | 80.5 ms                                                     | 89.2 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                       | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                     |
| xml_etree_parse      | 93.6 ms                                                     | 92.5 ms: 1.01x faster                                                     |
| json_dumps           | 5.92 ms                                                     | 6.14 ms: 1.04x slower                                                     |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.5 ms: 1.04x slower                                                     |
| xml_etree_generate   | 54.0 ms                                                     | 57.2 ms: 1.06x slower                                                     |
| xml_etree_process    | 37.0 ms                                                     | 40.3 ms: 1.09x slower                                                     |
| pickle_pure_python   | 190 us                                                      | 207 us: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.10x slower                                                      |
| tomli_loads          | 1.39 sec                                                    | 1.55 sec: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 21.3 ms: 1.20x faster                                                     |
| python_startup_no_site | 18.1 ms                                                     | 17.3 ms: 1.05x faster                                                     |
| Geometric mean         | (ref)                                                       | 1.12x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.84 ms: 1.08x slower                                                     |
| genshi_text     | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                     |
| django_template | 22.4 ms                                                     | 24.4 ms: 1.09x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 512 us: 17.17x faster                                                     |
| regex_v8                   | 21.4 ms                                                     | 14.4 ms: 1.49x faster                                                     |
| create_gc_cycles           | 1.26 ms                                                     | 888 us: 1.42x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.29x faster                                                     |
| bench_mp_pool              | 86.4 ms                                                     | 67.4 ms: 1.28x faster                                                     |
| python_startup             | 25.4 ms                                                     | 21.3 ms: 1.20x faster                                                     |
| deepcopy                   | 226 us                                                      | 190 us: 1.19x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 20.2 us: 1.16x faster                                                     |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                      |
| tornado_http               | 93.0 ms                                                     | 83.5 ms: 1.11x faster                                                     |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 74.2 ms: 1.09x faster                                                     |
| deepcopy_reduce            | 2.06 us                                                     | 1.93 us: 1.07x faster                                                     |
| json                       | 3.19 ms                                                     | 3.00 ms: 1.06x faster                                                     |
| async_tree_memoization     | 276 ms                                                      | 261 ms: 1.06x faster                                                      |
| bench_thread_pool          | 847 us                                                      | 807 us: 1.05x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                                      |
| python_startup_no_site     | 18.1 ms                                                     | 17.3 ms: 1.05x faster                                                     |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                     |
| go                         | 87.0 ms                                                     | 84.6 ms: 1.03x faster                                                     |
| regex_effbot               | 1.58 ms                                                     | 1.54 ms: 1.02x faster                                                     |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 92.5 ms: 1.01x faster                                                     |
| mdp                        | 1.39 sec                                                    | 1.40 sec: 1.01x slower                                                    |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                      |
| coverage                   | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                     |
| sympy_sum                  | 86.9 ms                                                     | 89.1 ms: 1.03x slower                                                     |
| html5lib                   | 38.9 ms                                                     | 40.0 ms: 1.03x slower                                                     |
| dulwich_log                | 40.8 ms                                                     | 42.1 ms: 1.03x slower                                                     |
| json_dumps                 | 5.92 ms                                                     | 6.14 ms: 1.04x slower                                                     |
| crypto_pyaes               | 45.4 ms                                                     | 47.2 ms: 1.04x slower                                                     |
| sympy_str                  | 169 ms                                                      | 175 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 110 us: 1.04x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 65.3 ms: 1.04x slower                                                     |
| sympy_integrate            | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.5 ms: 1.04x slower                                                     |
| sympy_expand               | 291 ms                                                      | 304 ms: 1.04x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.24 us: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 396 ms: 1.05x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.04 ms: 1.05x slower                                                     |
| xml_etree_generate         | 54.0 ms                                                     | 57.2 ms: 1.06x slower                                                     |
| meteor_contest             | 73.5 ms                                                     | 78.1 ms: 1.06x slower                                                     |
| logging_format             | 6.26 us                                                     | 6.67 us: 1.07x slower                                                     |
| docutils                   | 1.57 sec                                                    | 1.68 sec: 1.07x slower                                                    |
| mako                       | 6.35 ms                                                     | 6.84 ms: 1.08x slower                                                     |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.1 ms: 1.08x slower                                                     |
| genshi_text                | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                     |
| float                      | 49.9 ms                                                     | 54.2 ms: 1.08x slower                                                     |
| xml_etree_process          | 37.0 ms                                                     | 40.3 ms: 1.09x slower                                                     |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.67 ms: 1.09x slower                                                     |
| django_template            | 22.4 ms                                                     | 24.4 ms: 1.09x slower                                                     |
| pickle_pure_python         | 190 us                                                      | 207 us: 1.09x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 191 ms: 1.09x slower                                                      |
| async_tree_io              | 521 ms                                                      | 571 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 36.1 ms: 1.10x slower                                                     |
| pprint_safe_repr           | 494 ms                                                      | 541 ms: 1.10x slower                                                      |
| pycparser                  | 683 ms                                                      | 751 ms: 1.10x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                     |
| regex_compile              | 80.5 ms                                                     | 89.2 ms: 1.11x slower                                                     |
| pprint_pformat             | 999 ms                                                      | 1.11 sec: 1.11x slower                                                    |
| hexiom                     | 3.89 ms                                                     | 4.33 ms: 1.11x slower                                                     |
| tomli_loads                | 1.39 sec                                                    | 1.55 sec: 1.11x slower                                                    |
| chaos                      | 38.5 ms                                                     | 42.9 ms: 1.11x slower                                                     |
| pyflate                    | 283 ms                                                      | 316 ms: 1.12x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.5 us: 1.12x slower                                                     |
| nqueens                    | 56.7 ms                                                     | 63.7 ms: 1.12x slower                                                     |
| sqlglot_parse              | 771 us                                                      | 868 us: 1.13x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 61.7 ns: 1.13x slower                                                     |
| scimark_lu                 | 53.0 ms                                                     | 59.9 ms: 1.13x slower                                                     |
| scimark_sor                | 76.2 ms                                                     | 86.1 ms: 1.13x slower                                                     |
| sqlglot_transpile          | 956 us                                                      | 1.09 ms: 1.14x slower                                                     |
| fannkuch                   | 253 ms                                                      | 289 ms: 1.14x slower                                                      |
| raytrace                   | 160 ms                                                      | 184 ms: 1.15x slower                                                      |
| richards_super             | 30.9 ms                                                     | 35.5 ms: 1.15x slower                                                     |
| scimark_fft                | 172 ms                                                      | 199 ms: 1.15x slower                                                      |
| richards                   | 27.3 ms                                                     | 31.5 ms: 1.15x slower                                                     |
| deltablue                  | 1.92 ms                                                     | 2.23 ms: 1.16x slower                                                     |
| nbody                      | 68.4 ms                                                     | 82.1 ms: 1.20x slower                                                     |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.1 ms: 1.20x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                              |

Benchmark hidden because not significant (3): 2to3, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown