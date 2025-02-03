# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-amd64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.048x faster
- HPT reliability: 53.29%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.73 sec: 1.13x slower                                                      |
| sphinx         | 617 ms                                                      | 669 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                        |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 213 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 12.8 ms: 1.02x slower                                                       |
| async_generators           | 223 ms                                                      | 233 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 37.0 ms: 1.37x faster                                                       |
| nbody          | 66.3 ms                                                     | 50.4 ms: 1.32x faster                                                       |
| pidigits       | 146 ms                                                      | 150 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.8 ms: 1.62x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 110 us: 1.18x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.1 ms: 1.05x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.6 ms: 1.02x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.5 us: 1.03x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 198 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.26 ms: 1.25x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 17.1 ms: 1.12x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 43.3 ms: 1.28x slower                                                       |
| django_template | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 502 us: 16.86x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.8 ms: 1.62x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.5 us: 1.39x faster                                                       |
| float                      | 50.8 ms                                                     | 37.0 ms: 1.37x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 46.3 ms: 1.37x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 57.5 ms: 1.32x faster                                                       |
| nbody                      | 66.3 ms                                                     | 50.4 ms: 1.32x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                        |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 394 ms: 1.26x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.26 ms: 1.25x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 60.7 ms: 1.24x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 213 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.13 sec: 1.21x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.15 ms: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 185 us: 1.21x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.20x faster                                                       |
| scimark_fft                | 175 ms                                                      | 146 ms: 1.19x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 110 us: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 35.9 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.33 ms: 1.12x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.60 sec: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                       |
| pyflate                    | 283 ms                                                      | 267 ms: 1.06x faster                                                        |
| fannkuch                   | 252 ms                                                      | 237 ms: 1.06x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.62 sec: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.1 ms: 1.05x faster                                                       |
| shortest_path              | 355 ms                                                      | 346 ms: 1.03x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                       |
| connected_components       | 320 ms                                                      | 315 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.6 ms: 1.02x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 54.0 ns: 1.01x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 45.4 ms: 1.00x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.3 ms: 1.01x slower                                                       |
| coverage                   | 45.3 ms                                                     | 46.1 ms: 1.02x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 12.8 ms: 1.02x slower                                                       |
| pidigits                   | 146 ms                                                      | 150 ms: 1.03x slower                                                        |
| go                         | 84.7 ms                                                     | 87.0 ms: 1.03x slower                                                       |
| json_loads                 | 15.1 us                                                     | 15.5 us: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.03 ms: 1.03x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.04x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 843 us: 1.04x slower                                                        |
| async_generators           | 223 ms                                                      | 233 ms: 1.04x slower                                                        |
| sympy_expand               | 286 ms                                                      | 300 ms: 1.05x slower                                                        |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.05x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 809 us: 1.06x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 76.2 ms: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.3 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.6 ms: 1.06x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 198 us: 1.06x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 89.6 ms: 1.06x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.15 us: 1.06x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.59 us: 1.07x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.7 ms: 1.07x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.03 ms: 1.08x slower                                                       |
| sphinx                     | 617 ms                                                      | 669 ms: 1.08x slower                                                        |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 532 ms: 1.10x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 61.7 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 36.4 ms: 1.12x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 17.1 ms: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.13 ms: 1.13x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.73 sec: 1.13x slower                                                      |
| sqlglot_normalize          | 172 ms                                                      | 196 ms: 1.14x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.65 sec: 1.15x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                       |
| richards_super             | 29.8 ms                                                     | 35.8 ms: 1.20x slower                                                       |
| richards                   | 26.3 ms                                                     | 32.0 ms: 1.22x slower                                                       |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                                        |
| generators                 | 19.0 ms                                                     | 24.0 ms: 1.27x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.89 ms: 1.27x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 43.3 ms: 1.28x slower                                                       |
| django_template            | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                       |
| raytrace                   | 153 ms                                                      | 206 ms: 1.34x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 15.6 ms: 1.44x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (7): pylint, regex_dna, create_gc_cycles, html5lib, regex_compile, json_dumps, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 53.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown