# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.025x faster
- HPT reliability: 86.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.74 sec: 1.13x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 656 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_io              | 513 ms                                                      | 419 ms: 1.22x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 342 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 12.8 ms: 1.03x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 317 ms: 1.06x slower                                                        |
| async_generators           | 223 ms                                                      | 240 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 57.1 ms: 1.16x faster                                                       |
| float          | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                       |
| pidigits       | 146 ms                                                      | 152 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.0 ms: 1.59x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 82.2 ms: 1.02x slower                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.16x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 113 us: 1.15x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 50.8 ms: 1.05x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.1 ms: 1.01x slower                                                       |
| json_loads           | 15.1 us                                                     | 15.5 us: 1.02x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.69 ms: 1.08x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 217 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.24 ms: 1.25x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.4 ms: 1.05x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.0 ms: 1.05x slower                                                       |
| django_template | 20.3 ms                                                     | 25.8 ms: 1.27x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 516 us: 16.41x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.0 ms: 1.59x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.24 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.09 ms: 1.25x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 403 ms: 1.23x faster                                                        |
| async_tree_io              | 513 ms                                                      | 419 ms: 1.22x faster                                                        |
| pathlib                    | 75.3 ms                                                     | 62.1 ms: 1.21x faster                                                       |
| deepcopy                   | 223 us                                                      | 186 us: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.4 us: 1.19x faster                                                       |
| scimark_fft                | 175 ms                                                      | 148 ms: 1.18x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| nbody                      | 66.3 ms                                                     | 57.1 ms: 1.16x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.16x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 113 us: 1.15x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.56 sec: 1.12x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.51 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 342 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                        |
| float                      | 50.8 ms                                                     | 46.1 ms: 1.10x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 57.9 ms: 1.10x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.55 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.12 ms: 1.06x faster                                                       |
| fannkuch                   | 252 ms                                                      | 239 ms: 1.05x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 50.8 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.95 us: 1.04x faster                                                       |
| pyflate                    | 283 ms                                                      | 273 ms: 1.04x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.04x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 347 ms: 1.02x faster                                                        |
| connected_components       | 320 ms                                                      | 314 ms: 1.02x faster                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 45.8 ms: 1.00x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.1 ms: 1.01x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 82.2 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| json_loads                 | 15.1 us                                                     | 15.5 us: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 12.8 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                       |
| go                         | 84.7 ms                                                     | 87.6 ms: 1.03x slower                                                       |
| pidigits                   | 146 ms                                                      | 152 ms: 1.04x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.05 ms: 1.05x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.4 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 225 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 108 us: 1.05x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.0 ms: 1.05x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 75.8 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 855 us: 1.06x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 512 ms: 1.06x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 317 ms: 1.06x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.5 ms: 1.06x slower                                                       |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                        |
| generators                 | 19.0 ms                                                     | 20.2 ms: 1.06x slower                                                       |
| sphinx                     | 617 ms                                                      | 656 ms: 1.06x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 90.5 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.9 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 307 ms: 1.07x slower                                                        |
| async_generators           | 223 ms                                                      | 240 ms: 1.08x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 61.1 ms: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.69 ms: 1.08x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 59.5 ns: 1.09x slower                                                       |
| coverage                   | 45.3 ms                                                     | 49.6 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 842 us: 1.10x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.7 ms: 1.10x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.0 ms: 1.10x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 84.2 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.83 us: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.41 us: 1.11x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.4 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.06 ms: 1.11x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.60 sec: 1.12x slower                                                      |
| richards_super             | 29.8 ms                                                     | 33.6 ms: 1.13x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.7 ms: 1.13x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.74 sec: 1.13x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.42 ms: 1.15x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 37.6 ms: 1.16x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 217 us: 1.17x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 203 ms: 1.18x slower                                                        |
| many_optionals             | 361 us                                                      | 441 us: 1.22x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.34 ms: 1.24x slower                                                       |
| raytrace                   | 153 ms                                                      | 195 ms: 1.27x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.8 ms: 1.27x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (3): pylint, pprint_pformat, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 86.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown