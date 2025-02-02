# Results vs. 3.13.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-amd64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.037x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 228 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 43.0 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| async_tree_none            | 226 ms                                                      | 210 ms: 1.07x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 565 ms: 1.09x slower                                                       |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.9 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 56.9 ms: 1.14x slower                                                      |
| nbody          | 68.4 ms                                                     | 87.6 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.0 ms: 1.43x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 93.0 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.28 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.6 ms: 1.08x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 59.5 ms: 1.10x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 42.1 ms: 1.14x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 218 us: 1.15x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.62 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.7 ms: 1.12x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 18.6 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| mako            | 6.35 ms                                                     | 7.23 ms: 1.14x slower                                                      |
| django_template | 22.4 ms                                                     | 25.6 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 527 us: 16.69x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 15.0 ms: 1.43x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 884 us: 1.42x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.28x faster                                                      |
| deepcopy                   | 226 us                                                      | 188 us: 1.20x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 72.5 ms: 1.19x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.7 ms: 1.12x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 21.5 us: 1.08x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.91 us: 1.08x faster                                                      |
| async_tree_none            | 226 ms                                                      | 210 ms: 1.07x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.07x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.59 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 94.4 ms: 1.01x slower                                                      |
| telco                      | 4.79 ms                                                     | 4.87 ms: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                       |
| go                         | 87.0 ms                                                     | 88.9 ms: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 18.6 ms: 1.03x slower                                                      |
| 2to3                       | 221 ms                                                      | 228 ms: 1.03x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 90.4 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 110 us: 1.04x slower                                                       |
| coverage                   | 45.6 ms                                                     | 47.9 ms: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                       |
| sympy_expand               | 291 ms                                                      | 308 ms: 1.06x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.28 ms: 1.06x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 400 ms: 1.06x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 43.7 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.6 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| meteor_contest             | 73.5 ms                                                     | 79.5 ms: 1.08x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.47 us: 1.09x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 565 ms: 1.09x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.84 us: 1.09x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.52 sec: 1.09x slower                                                     |
| generators                 | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 59.5 ms: 1.10x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 43.0 ms: 1.10x slower                                                      |
| pycparser                  | 683 ms                                                      | 754 ms: 1.10x slower                                                       |
| async_tree_io              | 521 ms                                                      | 576 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 36.8 ms: 1.12x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 195 ms: 1.12x slower                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 50.9 ms: 1.12x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 554 ms: 1.12x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 42.1 ms: 1.14x slower                                                      |
| mako                       | 6.35 ms                                                     | 7.23 ms: 1.14x slower                                                      |
| float                      | 49.9 ms                                                     | 56.9 ms: 1.14x slower                                                      |
| django_template            | 22.4 ms                                                     | 25.6 ms: 1.14x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.14 sec: 1.14x slower                                                     |
| pickle_pure_python         | 190 us                                                      | 218 us: 1.15x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 93.0 ms: 1.15x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 65.5 ms: 1.16x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.84 ms: 1.16x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| pyflate                    | 283 ms                                                      | 329 ms: 1.16x slower                                                       |
| chaos                      | 38.5 ms                                                     | 44.8 ms: 1.16x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.62 sec: 1.16x slower                                                     |
| coroutines                 | 12.8 ms                                                     | 14.9 ms: 1.17x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 908 us: 1.18x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.13 ms: 1.18x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.63 ms: 1.19x slower                                                      |
| richards_super             | 30.9 ms                                                     | 36.8 ms: 1.19x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 74.9 ms: 1.19x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.6 ms: 1.20x slower                                                      |
| comprehensions             | 10.3 us                                                     | 12.3 us: 1.20x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.31 ms: 1.20x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 65.9 ns: 1.21x slower                                                      |
| fannkuch                   | 253 ms                                                      | 307 ms: 1.21x slower                                                       |
| raytrace                   | 160 ms                                                      | 198 ms: 1.24x slower                                                       |
| scimark_fft                | 172 ms                                                      | 214 ms: 1.24x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 51.3 ms: 1.26x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 96.2 ms: 1.26x slower                                                      |
| nbody                      | 68.4 ms                                                     | 87.6 ms: 1.28x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 67.9 ms: 1.28x slower                                                      |
| json                       | 3.19 ms                                                     | 4.15 ms: 1.30x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (5): bench_thread_pool, async_tree_none_tg, tornado_http, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown