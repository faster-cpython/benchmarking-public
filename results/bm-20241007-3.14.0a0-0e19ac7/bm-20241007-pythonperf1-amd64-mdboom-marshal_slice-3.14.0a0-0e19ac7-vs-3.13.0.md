# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: windows-amd64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.016x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 226 ms: 1.02x slower                                                |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                              |
| html5lib       | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                |
| async_tree_none            | 226 ms                                                      | 207 ms: 1.09x faster                                                |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                |
| async_tree_none_tg         | 209 ms                                                      | 201 ms: 1.04x faster                                                |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 384 ms: 1.02x slower                                                |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                               |
| async_tree_io_tg           | 518 ms                                                      | 566 ms: 1.09x slower                                                |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                |
| float          | 49.9 ms                                                     | 56.0 ms: 1.12x slower                                               |
| nbody          | 68.4 ms                                                     | 81.0 ms: 1.18x slower                                               |
| Geometric mean | (ref)                                                       | 1.11x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                               |
| regex_effbot   | 1.58 ms                                                     | 1.54 ms: 1.02x faster                                               |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                |
| regex_compile  | 80.5 ms                                                     | 90.4 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                       | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                               |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.4 ms: 1.04x slower                                               |
| json_dumps           | 5.92 ms                                                     | 6.28 ms: 1.06x slower                                               |
| xml_etree_generate   | 54.0 ms                                                     | 58.0 ms: 1.07x slower                                               |
| xml_etree_process    | 37.0 ms                                                     | 40.7 ms: 1.10x slower                                               |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.12x slower                                                |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                              |
| pickle_pure_python   | 190 us                                                      | 215 us: 1.13x slower                                                |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.1 ms: 1.15x faster                                               |
| python_startup_no_site | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                               |
| Geometric mean         | (ref)                                                       | 1.08x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 16.8 ms: 1.08x slower                                               |
| mako            | 6.35 ms                                                     | 6.93 ms: 1.09x slower                                               |
| django_template | 22.4 ms                                                     | 24.8 ms: 1.11x slower                                               |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 513 us: 17.14x faster                                               |
| regex_v8                   | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                               |
| create_gc_cycles           | 1.26 ms                                                     | 917 us: 1.37x faster                                                |
| gc_traversal               | 1.97 ms                                                     | 1.57 ms: 1.26x faster                                               |
| bench_mp_pool              | 86.4 ms                                                     | 68.9 ms: 1.25x faster                                               |
| deepcopy                   | 226 us                                                      | 185 us: 1.22x faster                                                |
| deepcopy_memo              | 23.3 us                                                     | 20.1 us: 1.16x faster                                               |
| python_startup             | 25.4 ms                                                     | 22.1 ms: 1.15x faster                                               |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.14x faster                                                |
| async_tree_none            | 226 ms                                                      | 207 ms: 1.09x faster                                                |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                               |
| deepcopy_reduce            | 2.06 us                                                     | 1.95 us: 1.06x faster                                               |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                |
| async_tree_none_tg         | 209 ms                                                      | 201 ms: 1.04x faster                                                |
| pathlib                    | 80.9 ms                                                     | 78.8 ms: 1.03x faster                                               |
| regex_effbot               | 1.58 ms                                                     | 1.54 ms: 1.02x faster                                               |
| python_startup_no_site     | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                               |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                |
| telco                      | 4.79 ms                                                     | 4.84 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.02x slower                                                |
| mdp                        | 1.39 sec                                                    | 1.41 sec: 1.02x slower                                              |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 384 ms: 1.02x slower                                                |
| 2to3                       | 221 ms                                                      | 226 ms: 1.02x slower                                                |
| html5lib                   | 38.9 ms                                                     | 40.1 ms: 1.03x slower                                               |
| sympy_sum                  | 86.9 ms                                                     | 90.0 ms: 1.04x slower                                               |
| meteor_contest             | 73.5 ms                                                     | 76.3 ms: 1.04x slower                                               |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.4 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 105 us                                                      | 110 us: 1.04x slower                                                |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.05x slower                                                |
| sympy_expand               | 291 ms                                                      | 307 ms: 1.05x slower                                                |
| pycparser                  | 683 ms                                                      | 720 ms: 1.05x slower                                                |
| json_dumps                 | 5.92 ms                                                     | 6.28 ms: 1.06x slower                                               |
| logging_simple             | 5.96 us                                                     | 6.33 us: 1.06x slower                                               |
| sympy_integrate            | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                               |
| dulwich_log                | 40.8 ms                                                     | 43.8 ms: 1.07x slower                                               |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.07x slower                                               |
| xml_etree_generate         | 54.0 ms                                                     | 58.0 ms: 1.07x slower                                               |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                              |
| genshi_text                | 15.6 ms                                                     | 16.8 ms: 1.08x slower                                               |
| coverage                   | 45.6 ms                                                     | 49.2 ms: 1.08x slower                                               |
| crypto_pyaes               | 45.4 ms                                                     | 49.3 ms: 1.09x slower                                               |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                               |
| logging_format             | 6.26 us                                                     | 6.82 us: 1.09x slower                                               |
| mako                       | 6.35 ms                                                     | 6.93 ms: 1.09x slower                                               |
| async_tree_io_tg           | 518 ms                                                      | 566 ms: 1.09x slower                                                |
| spectral_norm              | 62.8 ms                                                     | 68.8 ms: 1.10x slower                                               |
| sqlglot_normalize          | 175 ms                                                      | 192 ms: 1.10x slower                                                |
| async_tree_io              | 521 ms                                                      | 573 ms: 1.10x slower                                                |
| pprint_safe_repr           | 494 ms                                                      | 542 ms: 1.10x slower                                                |
| xml_etree_process          | 37.0 ms                                                     | 40.7 ms: 1.10x slower                                               |
| sqlglot_optimize           | 32.9 ms                                                     | 36.3 ms: 1.10x slower                                               |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                |
| django_template            | 22.4 ms                                                     | 24.8 ms: 1.11x slower                                               |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.72 ms: 1.11x slower                                               |
| pprint_pformat             | 999 ms                                                      | 1.11 sec: 1.11x slower                                              |
| float                      | 49.9 ms                                                     | 56.0 ms: 1.12x slower                                               |
| hexiom                     | 3.89 ms                                                     | 4.37 ms: 1.12x slower                                               |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.12x slower                                                |
| regex_compile              | 80.5 ms                                                     | 90.4 ms: 1.12x slower                                               |
| pyflate                    | 283 ms                                                      | 319 ms: 1.13x slower                                                |
| chaos                      | 38.5 ms                                                     | 43.5 ms: 1.13x slower                                               |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                              |
| pickle_pure_python         | 190 us                                                      | 215 us: 1.13x slower                                                |
| fannkuch                   | 253 ms                                                      | 288 ms: 1.14x slower                                                |
| nqueens                    | 56.7 ms                                                     | 64.6 ms: 1.14x slower                                               |
| sqlglot_parse              | 771 us                                                      | 880 us: 1.14x slower                                                |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                               |
| sqlglot_transpile          | 956 us                                                      | 1.10 ms: 1.15x slower                                               |
| logging_silent             | 54.6 ns                                                     | 63.1 ns: 1.16x slower                                               |
| richards_super             | 30.9 ms                                                     | 36.2 ms: 1.17x slower                                               |
| richards                   | 27.3 ms                                                     | 32.2 ms: 1.18x slower                                               |
| nbody                      | 68.4 ms                                                     | 81.0 ms: 1.18x slower                                               |
| scimark_monte_carlo        | 40.8 ms                                                     | 48.4 ms: 1.19x slower                                               |
| scimark_sor                | 76.2 ms                                                     | 90.4 ms: 1.19x slower                                               |
| deltablue                  | 1.92 ms                                                     | 2.28 ms: 1.19x slower                                               |
| scimark_fft                | 172 ms                                                      | 205 ms: 1.19x slower                                                |
| raytrace                   | 160 ms                                                      | 198 ms: 1.24x slower                                                |
| scimark_lu                 | 53.0 ms                                                     | 65.8 ms: 1.24x slower                                               |
| json                       | 3.19 ms                                                     | 4.27 ms: 1.34x slower                                               |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                        |

Benchmark hidden because not significant (6): bench_thread_pool, tornado_http, xml_etree_parse, go, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.016x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown