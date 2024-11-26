# Results vs. 3.13.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-amd64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.003x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| tornado_http   | 93.0 ms                                                     | 83.3 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| async_tree_none            | 226 ms                                                      | 207 ms: 1.09x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 259 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 197 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 390 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 238 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 553 ms: 1.07x slower                                                       |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 54.4 ms: 1.09x slower                                                      |
| nbody          | 68.4 ms                                                     | 79.8 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.6 ms: 1.47x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_compile  | 80.5 ms                                                     | 89.6 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 6.18 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.8 ms: 1.05x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.2 ms: 1.06x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 145 us: 1.08x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 40.4 ms: 1.09x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 209 us: 1.10x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.56 sec: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 21.3 ms: 1.19x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 17.3 ms: 1.05x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.83 ms: 1.08x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                      |
| django_template | 22.4 ms                                                     | 24.5 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 507 us: 17.34x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.6 ms: 1.47x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 887 us: 1.42x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 65.8 ms: 1.31x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.52 ms: 1.29x faster                                                      |
| deepcopy                   | 226 us                                                      | 188 us: 1.21x faster                                                       |
| python_startup             | 25.4 ms                                                     | 21.3 ms: 1.19x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 20.0 us: 1.17x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                       |
| tornado_http               | 93.0 ms                                                     | 83.3 ms: 1.12x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 73.9 ms: 1.09x faster                                                      |
| async_tree_none            | 226 ms                                                      | 207 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.07x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 259 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 197 ms: 1.06x faster                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.3 ms: 1.05x faster                                                      |
| bench_thread_pool          | 847 us                                                      | 810 us: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| go                         | 87.0 ms                                                     | 84.6 ms: 1.03x faster                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                      |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                      | 151 ms: 1.02x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 89.2 ms: 1.03x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 41.9 ms: 1.03x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 64.7 ms: 1.03x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 46.9 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 390 ms: 1.03x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.18 ms: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 176 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.8 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 111 us: 1.05x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.25 us: 1.05x slower                                                      |
| sympy_expand               | 291 ms                                                      | 306 ms: 1.05x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 77.6 ms: 1.06x slower                                                      |
| coverage                   | 45.6 ms                                                     | 48.1 ms: 1.06x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.06 ms: 1.06x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 57.2 ms: 1.06x slower                                                      |
| async_generators           | 223 ms                                                      | 238 ms: 1.06x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.66 us: 1.06x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 553 ms: 1.07x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.07x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.64 ms: 1.07x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.83 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.08x slower                                                     |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                     |
| async_tree_io              | 521 ms                                                      | 564 ms: 1.08x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 16.9 ms: 1.08x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 145 us: 1.08x slower                                                       |
| float                      | 49.9 ms                                                     | 54.4 ms: 1.09x slower                                                      |
| pycparser                  | 683 ms                                                      | 744 ms: 1.09x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 40.4 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 36.0 ms: 1.09x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 191 ms: 1.09x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 541 ms: 1.10x slower                                                       |
| django_template            | 22.4 ms                                                     | 24.5 ms: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                      |
| chaos                      | 38.5 ms                                                     | 42.3 ms: 1.10x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 209 us: 1.10x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.30 ms: 1.10x slower                                                      |
| fannkuch                   | 253 ms                                                      | 280 ms: 1.11x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 62.9 ms: 1.11x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.11 sec: 1.11x slower                                                     |
| regex_compile              | 80.5 ms                                                     | 89.6 ms: 1.11x slower                                                      |
| pyflate                    | 283 ms                                                      | 315 ms: 1.11x slower                                                       |
| comprehensions             | 10.3 us                                                     | 11.4 us: 1.11x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.56 sec: 1.12x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 61.9 ns: 1.13x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 875 us: 1.14x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.09 ms: 1.14x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 87.5 ms: 1.15x slower                                                      |
| richards                   | 27.3 ms                                                     | 31.7 ms: 1.16x slower                                                      |
| richards_super             | 30.9 ms                                                     | 35.8 ms: 1.16x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.24 ms: 1.17x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 61.8 ms: 1.17x slower                                                      |
| nbody                      | 68.4 ms                                                     | 79.8 ms: 1.17x slower                                                      |
| raytrace                   | 160 ms                                                      | 187 ms: 1.17x slower                                                       |
| scimark_fft                | 172 ms                                                      | 204 ms: 1.18x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 48.5 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (7): json, 2to3, xml_etree_parse, genshi_xml, html5lib, async_tree_cpu_io_mixed, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-pythonperf1-amd64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown