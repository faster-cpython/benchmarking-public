# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-amd64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.027x faster
- HPT reliability: 52.49%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.73 sec: 1.13x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.6 ms: 1.04x slower                                                       |
| sphinx         | 617 ms                                                      | 675 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 403 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                        |
| async_tree_none            | 219 ms                                                      | 184 ms: 1.19x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 353 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 53.0 ms: 1.25x faster                                                       |
| float          | 50.8 ms                                                     | 45.9 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.42 ms: 1.20x faster                                                       |
| regex_v8       | 23.8 ms                                                     | 20.2 ms: 1.18x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 80.4 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 110 us: 1.18x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.15x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 85.9 ms: 1.07x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 50.5 ms: 1.06x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 58.8 ms: 1.03x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 6.41 ms: 1.03x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.3 ms: 1.05x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.5 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.13 ms: 1.28x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 18.7 ms: 1.23x slower                                                       |
| django_template | 20.3 ms                                                     | 27.1 ms: 1.34x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 46.2 ms: 1.36x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 512 us: 16.53x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.8 us: 1.38x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 49.4 ms: 1.28x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.13 ms: 1.28x faster                                                       |
| async_tree_io              | 513 ms                                                      | 403 ms: 1.27x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.05 ms: 1.27x faster                                                       |
| nbody                      | 66.3 ms                                                     | 53.0 ms: 1.25x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                        |
| scimark_fft                | 175 ms                                                      | 143 ms: 1.22x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.42 ms: 1.20x faster                                                       |
| async_tree_none            | 219 ms                                                      | 184 ms: 1.19x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 63.9 ms: 1.19x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 20.2 ms: 1.18x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 110 us: 1.18x faster                                                        |
| deepcopy                   | 223 us                                                      | 191 us: 1.17x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.16x faster                                                        |
| json                       | 3.30 ms                                                     | 2.87 ms: 1.15x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.15x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.27 ms: 1.14x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 40.8 ms: 1.12x faster                                                       |
| float                      | 50.8 ms                                                     | 45.9 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 37.4 ms: 1.09x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.64 sec: 1.09x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 353 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 85.9 ms: 1.07x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.60 sec: 1.06x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.5 ms: 1.06x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.3 ms: 1.05x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 54.7 ms: 1.04x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.8 ms: 1.03x faster                                                       |
| connected_components       | 320 ms                                                      | 311 ms: 1.03x faster                                                        |
| shortest_path              | 355 ms                                                      | 346 ms: 1.03x faster                                                        |
| fannkuch                   | 252 ms                                                      | 246 ms: 1.02x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 82.7 ms: 1.02x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 80.4 ms: 1.00x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 996 ms: 1.02x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.0 ms: 1.02x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 830 us: 1.02x slower                                                        |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 497 ms: 1.03x slower                                                        |
| pathlib                    | 75.3 ms                                                     | 77.4 ms: 1.03x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.1 ms: 1.03x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.3 ns: 1.03x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.5 ms: 1.03x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.41 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.6 ms: 1.04x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.1 ms: 1.04x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.50 sec: 1.05x slower                                                      |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                        |
| sympy_expand               | 286 ms                                                      | 303 ms: 1.06x slower                                                        |
| go                         | 84.7 ms                                                     | 89.9 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.1 ms: 1.07x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.3 ms: 1.09x slower                                                       |
| sphinx                     | 617 ms                                                      | 675 ms: 1.09x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.10x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 844 us: 1.10x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.88 us: 1.11x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.43 us: 1.11x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.73 sec: 1.13x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.09 ms: 1.14x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.15x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 37.8 ms: 1.16x slower                                                       |
| async_generators           | 223 ms                                                      | 260 ms: 1.17x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 66.6 ms: 1.19x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 206 ms: 1.20x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.28 ms: 1.20x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 18.7 ms: 1.23x slower                                                       |
| generators                 | 19.0 ms                                                     | 23.6 ms: 1.24x slower                                                       |
| many_optionals             | 361 us                                                      | 457 us: 1.27x slower                                                        |
| richards                   | 26.3 ms                                                     | 33.7 ms: 1.28x slower                                                       |
| richards_super             | 29.8 ms                                                     | 38.4 ms: 1.29x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 5.06 ms: 1.32x slower                                                       |
| django_template            | 20.3 ms                                                     | 27.1 ms: 1.34x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 46.2 ms: 1.36x slower                                                       |
| raytrace                   | 153 ms                                                      | 212 ms: 1.38x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (6): pidigits, gc_traversal, asyncio_websockets, pylint, pyflate, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: mypy2

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 52.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown