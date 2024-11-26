# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-amd64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                 |
| html5lib       | 38.9 ms                                                     | 40.3 ms: 1.03x slower                                                  |
| tornado_http   | 93.0 ms                                                     | 84.1 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                       | 1.00x slower                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                                   |
| async_tree_none            | 226 ms                                                      | 205 ms: 1.10x faster                                                   |
| async_tree_memoization     | 276 ms                                                      | 259 ms: 1.07x faster                                                   |
| async_tree_none_tg         | 209 ms                                                      | 201 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                   |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                   |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                   |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.08x slower                                                   |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                   |
| float          | 49.9 ms                                                     | 56.6 ms: 1.13x slower                                                  |
| nbody          | 68.4 ms                                                     | 81.8 ms: 1.20x slower                                                  |
| Geometric mean | (ref)                                                       | 1.11x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.1 ms: 1.42x faster                                                  |
| regex_effbot   | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                  |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                   |
| regex_compile  | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                       | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.1 ms: 1.05x slower                                                  |
| json_dumps           | 5.92 ms                                                     | 6.23 ms: 1.05x slower                                                  |
| xml_etree_generate   | 54.0 ms                                                     | 58.6 ms: 1.09x slower                                                  |
| xml_etree_process    | 37.0 ms                                                     | 40.8 ms: 1.10x slower                                                  |
| pickle_pure_python   | 190 us                                                      | 212 us: 1.12x slower                                                   |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.14x slower                                                   |
| tomli_loads          | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 21.4 ms: 1.19x faster                                                  |
| python_startup_no_site | 18.1 ms                                                     | 17.5 ms: 1.04x faster                                                  |
| Geometric mean         | (ref)                                                       | 1.11x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 37.4 ms: 1.05x slower                                                  |
| mako            | 6.35 ms                                                     | 6.89 ms: 1.08x slower                                                  |
| genshi_text     | 15.6 ms                                                     | 17.3 ms: 1.11x slower                                                  |
| django_template | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 544 us: 16.16x faster                                                  |
| create_gc_cycles           | 1.26 ms                                                     | 878 us: 1.43x faster                                                   |
| regex_v8                   | 21.4 ms                                                     | 15.1 ms: 1.42x faster                                                  |
| bench_mp_pool              | 86.4 ms                                                     | 66.6 ms: 1.30x faster                                                  |
| gc_traversal               | 1.97 ms                                                     | 1.52 ms: 1.29x faster                                                  |
| deepcopy                   | 226 us                                                      | 188 us: 1.20x faster                                                   |
| python_startup             | 25.4 ms                                                     | 21.4 ms: 1.19x faster                                                  |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.14x faster                                                   |
| deepcopy_memo              | 23.3 us                                                     | 20.6 us: 1.13x faster                                                  |
| tornado_http               | 93.0 ms                                                     | 84.1 ms: 1.11x faster                                                  |
| pathlib                    | 80.9 ms                                                     | 73.5 ms: 1.10x faster                                                  |
| async_tree_none            | 226 ms                                                      | 205 ms: 1.10x faster                                                   |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.07x faster                                                  |
| async_tree_memoization     | 276 ms                                                      | 259 ms: 1.07x faster                                                   |
| bench_thread_pool          | 847 us                                                      | 805 us: 1.05x faster                                                   |
| python_startup_no_site     | 18.1 ms                                                     | 17.5 ms: 1.04x faster                                                  |
| async_tree_none_tg         | 209 ms                                                      | 201 ms: 1.04x faster                                                   |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                  |
| regex_effbot               | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 390 ms: 1.02x slower                                                   |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                   |
| coverage                   | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                  |
| html5lib                   | 38.9 ms                                                     | 40.3 ms: 1.03x slower                                                  |
| dulwich_log                | 40.8 ms                                                     | 42.6 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                   |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                   |
| sympy_sum                  | 86.9 ms                                                     | 91.2 ms: 1.05x slower                                                  |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.1 ms: 1.05x slower                                                  |
| json_dumps                 | 5.92 ms                                                     | 6.23 ms: 1.05x slower                                                  |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                   |
| genshi_xml                 | 35.5 ms                                                     | 37.4 ms: 1.05x slower                                                  |
| sympy_expand               | 291 ms                                                      | 307 ms: 1.05x slower                                                   |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                   |
| meteor_contest             | 73.5 ms                                                     | 77.9 ms: 1.06x slower                                                  |
| sympy_integrate            | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                  |
| crypto_pyaes               | 45.4 ms                                                     | 48.1 ms: 1.06x slower                                                  |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                   |
| logging_simple             | 5.96 us                                                     | 6.39 us: 1.07x slower                                                  |
| telco                      | 4.79 ms                                                     | 5.16 ms: 1.08x slower                                                  |
| generators                 | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                  |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                   |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                 |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                 |
| mako                       | 6.35 ms                                                     | 6.89 ms: 1.08x slower                                                  |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.08x slower                                                   |
| xml_etree_generate         | 54.0 ms                                                     | 58.6 ms: 1.09x slower                                                  |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                  |
| spectral_norm              | 62.8 ms                                                     | 69.0 ms: 1.10x slower                                                  |
| logging_format             | 6.26 us                                                     | 6.88 us: 1.10x slower                                                  |
| sqlglot_normalize          | 175 ms                                                      | 193 ms: 1.10x slower                                                   |
| xml_etree_process          | 37.0 ms                                                     | 40.8 ms: 1.10x slower                                                  |
| pprint_safe_repr           | 494 ms                                                      | 546 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.72 ms: 1.11x slower                                                  |
| genshi_text                | 15.6 ms                                                     | 17.3 ms: 1.11x slower                                                  |
| sqlglot_optimize           | 32.9 ms                                                     | 36.5 ms: 1.11x slower                                                  |
| pprint_pformat             | 999 ms                                                      | 1.11 sec: 1.11x slower                                                 |
| django_template            | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                  |
| pickle_pure_python         | 190 us                                                      | 212 us: 1.12x slower                                                   |
| nqueens                    | 56.7 ms                                                     | 63.7 ms: 1.12x slower                                                  |
| pyflate                    | 283 ms                                                      | 319 ms: 1.13x slower                                                   |
| hexiom                     | 3.89 ms                                                     | 4.39 ms: 1.13x slower                                                  |
| chaos                      | 38.5 ms                                                     | 43.7 ms: 1.13x slower                                                  |
| float                      | 49.9 ms                                                     | 56.6 ms: 1.13x slower                                                  |
| comprehensions             | 10.3 us                                                     | 11.7 us: 1.14x slower                                                  |
| regex_compile              | 80.5 ms                                                     | 91.5 ms: 1.14x slower                                                  |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.14x slower                                                   |
| tomli_loads                | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                 |
| logging_silent             | 54.6 ns                                                     | 62.6 ns: 1.15x slower                                                  |
| fannkuch                   | 253 ms                                                      | 292 ms: 1.15x slower                                                   |
| scimark_sor                | 76.2 ms                                                     | 88.8 ms: 1.17x slower                                                  |
| sqlglot_parse              | 771 us                                                      | 900 us: 1.17x slower                                                   |
| sqlglot_transpile          | 956 us                                                      | 1.12 ms: 1.17x slower                                                  |
| raytrace                   | 160 ms                                                      | 188 ms: 1.17x slower                                                   |
| pycparser                  | 683 ms                                                      | 802 ms: 1.17x slower                                                   |
| scimark_fft                | 172 ms                                                      | 203 ms: 1.18x slower                                                   |
| richards_super             | 30.9 ms                                                     | 36.4 ms: 1.18x slower                                                  |
| deltablue                  | 1.92 ms                                                     | 2.26 ms: 1.18x slower                                                  |
| richards                   | 27.3 ms                                                     | 32.4 ms: 1.19x slower                                                  |
| nbody                      | 68.4 ms                                                     | 81.8 ms: 1.20x slower                                                  |
| scimark_lu                 | 53.0 ms                                                     | 63.6 ms: 1.20x slower                                                  |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.9 ms: 1.22x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                           |

Benchmark hidden because not significant (5): json, xml_etree_parse, go, 2to3, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown