# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: windows-amd64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.023x faster
- HPT reliability: 98.78%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 216 ms: 1.02x faster                                              |
| chameleon      | 4.82 ms                                                     | 4.89 ms: 1.01x slower                                             |
| docutils       | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                            |
| html5lib       | 38.9 ms                                                     | 40.2 ms: 1.03x slower                                             |
| tornado_http   | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                       | 1.00x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none_tg         | 209 ms                                                      | 203 ms: 1.03x faster                                              |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                              |
| async_tree_io_tg           | 518 ms                                                      | 506 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 374 ms: 1.02x faster                                              |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 370 ms: 1.02x faster                                              |
| coroutines                 | 12.8 ms                                                     | 13.1 ms: 1.03x slower                                             |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                      |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 50.3 ms: 1.01x slower                                             |
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                              |
| nbody          | 68.4 ms                                                     | 71.0 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 17.1 ms: 1.25x faster                                             |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                              |
| regex_compile  | 80.5 ms                                                     | 83.8 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                       | 1.04x faster                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                             |
| pickle_pure_python   | 190 us                                                      | 183 us: 1.03x faster                                              |
| xml_etree_parse      | 93.6 ms                                                     | 90.9 ms: 1.03x faster                                             |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.03x faster                                              |
| json_dumps           | 5.92 ms                                                     | 5.78 ms: 1.02x faster                                             |
| xml_etree_generate   | 54.0 ms                                                     | 53.0 ms: 1.02x faster                                             |
| xml_etree_iterparse  | 61.8 ms                                                     | 61.1 ms: 1.01x faster                                             |
| xml_etree_process    | 37.0 ms                                                     | 36.7 ms: 1.01x faster                                             |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                      |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.4 ms: 1.14x faster                                             |
| python_startup_no_site | 18.1 ms                                                     | 17.9 ms: 1.02x faster                                             |
| Geometric mean         | (ref)                                                       | 1.07x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 22.4 ms                                                     | 22.1 ms: 1.01x faster                                             |
| genshi_text     | 15.6 ms                                                     | 15.5 ms: 1.01x faster                                             |
| mako            | 6.35 ms                                                     | 6.68 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mypy2                      | 679 ms                                                      | 431 ms: 1.58x faster                                              |
| create_gc_cycles           | 1.26 ms                                                     | 807 us: 1.56x faster                                              |
| gc_traversal               | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                             |
| regex_v8                   | 21.4 ms                                                     | 17.1 ms: 1.25x faster                                             |
| bench_mp_pool              | 86.4 ms                                                     | 69.3 ms: 1.25x faster                                             |
| python_startup             | 25.4 ms                                                     | 22.4 ms: 1.14x faster                                             |
| bench_thread_pool          | 847 us                                                      | 786 us: 1.08x faster                                              |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                             |
| json                       | 3.19 ms                                                     | 2.99 ms: 1.07x faster                                             |
| logging_simple             | 5.96 us                                                     | 5.70 us: 1.05x faster                                             |
| telco                      | 4.79 ms                                                     | 4.61 ms: 1.04x faster                                             |
| richards_super             | 30.9 ms                                                     | 29.8 ms: 1.04x faster                                             |
| typing_runtime_protocols   | 105 us                                                      | 102 us: 1.04x faster                                              |
| richards                   | 27.3 ms                                                     | 26.4 ms: 1.03x faster                                             |
| pickle_pure_python         | 190 us                                                      | 183 us: 1.03x faster                                              |
| async_tree_none_tg         | 209 ms                                                      | 203 ms: 1.03x faster                                              |
| xml_etree_parse            | 93.6 ms                                                     | 90.9 ms: 1.03x faster                                             |
| fannkuch                   | 253 ms                                                      | 246 ms: 1.03x faster                                              |
| logging_silent             | 54.6 ns                                                     | 53.2 ns: 1.03x faster                                             |
| unpickle_pure_python       | 133 us                                                      | 130 us: 1.03x faster                                              |
| async_tree_none            | 226 ms                                                      | 220 ms: 1.03x faster                                              |
| async_tree_io_tg           | 518 ms                                                      | 506 ms: 1.02x faster                                              |
| logging_format             | 6.26 us                                                     | 6.11 us: 1.02x faster                                             |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 374 ms: 1.02x faster                                              |
| json_dumps                 | 5.92 ms                                                     | 5.78 ms: 1.02x faster                                             |
| sympy_expand               | 291 ms                                                      | 285 ms: 1.02x faster                                              |
| deepcopy_memo              | 23.3 us                                                     | 22.8 us: 1.02x faster                                             |
| 2to3                       | 221 ms                                                      | 216 ms: 1.02x faster                                              |
| spectral_norm              | 62.8 ms                                                     | 61.5 ms: 1.02x faster                                             |
| deepcopy_reduce            | 2.06 us                                                     | 2.02 us: 1.02x faster                                             |
| pathlib                    | 80.9 ms                                                     | 79.3 ms: 1.02x faster                                             |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                              |
| xml_etree_generate         | 54.0 ms                                                     | 53.0 ms: 1.02x faster                                             |
| go                         | 87.0 ms                                                     | 85.4 ms: 1.02x faster                                             |
| mdp                        | 1.39 sec                                                    | 1.36 sec: 1.02x faster                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 370 ms: 1.02x faster                                              |
| python_startup_no_site     | 18.1 ms                                                     | 17.9 ms: 1.02x faster                                             |
| django_template            | 22.4 ms                                                     | 22.1 ms: 1.01x faster                                             |
| hexiom                     | 3.89 ms                                                     | 3.85 ms: 1.01x faster                                             |
| xml_etree_iterparse        | 61.8 ms                                                     | 61.1 ms: 1.01x faster                                             |
| thrift                     | 8.80 ms                                                     | 8.70 ms: 1.01x faster                                             |
| xml_etree_process          | 37.0 ms                                                     | 36.7 ms: 1.01x faster                                             |
| tornado_http               | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                             |
| sympy_str                  | 169 ms                                                      | 167 ms: 1.01x faster                                              |
| pyflate                    | 283 ms                                                      | 281 ms: 1.01x faster                                              |
| deltablue                  | 1.92 ms                                                     | 1.90 ms: 1.01x faster                                             |
| genshi_text                | 15.6 ms                                                     | 15.5 ms: 1.01x faster                                             |
| docutils                   | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                            |
| sympy_integrate            | 12.5 ms                                                     | 12.4 ms: 1.00x faster                                             |
| nqueens                    | 56.7 ms                                                     | 56.9 ms: 1.00x slower                                             |
| pprint_pformat             | 999 ms                                                      | 1.00 sec: 1.01x slower                                            |
| crypto_pyaes               | 45.4 ms                                                     | 45.7 ms: 1.01x slower                                             |
| scimark_monte_carlo        | 40.8 ms                                                     | 41.1 ms: 1.01x slower                                             |
| coverage                   | 45.6 ms                                                     | 45.9 ms: 1.01x slower                                             |
| float                      | 49.9 ms                                                     | 50.3 ms: 1.01x slower                                             |
| scimark_sor                | 76.2 ms                                                     | 76.9 ms: 1.01x slower                                             |
| dulwich_log                | 40.8 ms                                                     | 41.4 ms: 1.01x slower                                             |
| chameleon                  | 4.82 ms                                                     | 4.89 ms: 1.01x slower                                             |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                              |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.50 ms: 1.02x slower                                             |
| sqlglot_optimize           | 32.9 ms                                                     | 33.5 ms: 1.02x slower                                             |
| comprehensions             | 10.3 us                                                     | 10.5 us: 1.02x slower                                             |
| scimark_fft                | 172 ms                                                      | 176 ms: 1.02x slower                                              |
| sqlglot_parse              | 771 us                                                      | 789 us: 1.02x slower                                              |
| sqlglot_transpile          | 956 us                                                      | 980 us: 1.02x slower                                              |
| chaos                      | 38.5 ms                                                     | 39.5 ms: 1.03x slower                                             |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                              |
| coroutines                 | 12.8 ms                                                     | 13.1 ms: 1.03x slower                                             |
| generators                 | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                             |
| raytrace                   | 160 ms                                                      | 165 ms: 1.03x slower                                              |
| html5lib                   | 38.9 ms                                                     | 40.2 ms: 1.03x slower                                             |
| nbody                      | 68.4 ms                                                     | 71.0 ms: 1.04x slower                                             |
| regex_compile              | 80.5 ms                                                     | 83.8 ms: 1.04x slower                                             |
| mako                       | 6.35 ms                                                     | 6.68 ms: 1.05x slower                                             |
| scimark_lu                 | 53.0 ms                                                     | 57.2 ms: 1.08x slower                                             |
| pycparser                  | 683 ms                                                      | 758 ms: 1.11x slower                                              |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                      |

Benchmark hidden because not significant (12): genshi_xml, async_tree_memoization, pylint, async_tree_io, async_tree_memoization_tg, regex_effbot, tomli_loads, pprint_safe_repr, deepcopy, sympy_sum, sqlglot_normalize, meteor_contest
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 98.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown