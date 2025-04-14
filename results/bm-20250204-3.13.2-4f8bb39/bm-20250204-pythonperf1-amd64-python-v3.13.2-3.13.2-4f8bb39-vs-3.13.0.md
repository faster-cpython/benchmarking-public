# Results vs. 3.13.0

- fork: python
- ref: v3.13.2
- machine: windows-amd64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.006x faster
- HPT reliability: 88.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                        |
| docutils       | 1.53 sec                                                    | 1.54 sec: 1.01x slower                                      |
| tornado_http   | 81.2 ms                                                     | 100 ms: 1.23x slower                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                |

Benchmark hidden because not significant (3): chameleon, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_generators           | 223 ms                                                      | 211 ms: 1.06x faster                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 277 ms: 1.01x faster                                        |
| coroutines                 | 12.5 ms                                                     | 12.7 ms: 1.02x slower                                       |
| async_tree_none            | 219 ms                                                      | 224 ms: 1.02x slower                                        |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 406 ms: 1.06x slower                                        |
| async_tree_io_tg           | 497 ms                                                      | 527 ms: 1.06x slower                                        |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 50.8 ms                                                     | 47.7 ms: 1.07x faster                                       |
| nbody          | 66.3 ms                                                     | 65.1 ms: 1.02x faster                                       |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.0 ms: 1.59x faster                                       |
| regex_effbot   | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.01x faster                                        |
| regex_compile  | 80.7 ms                                                     | 79.8 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|---------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps          | 6.19 ms                                                     | 5.84 ms: 1.06x faster                                       |
| json_loads          | 15.1 us                                                     | 14.5 us: 1.04x faster                                       |
| xml_etree_parse     | 92.2 ms                                                     | 91.4 ms: 1.01x faster                                       |
| pickle_pure_python  | 186 us                                                      | 189 us: 1.02x slower                                        |
| xml_etree_iterparse | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                       |
| Geometric mean      | (ref)                                                       | 1.00x faster                                                |

Benchmark hidden because not significant (4): xml_etree_process, unpickle_pure_python, tomli_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                       |
| python_startup_no_site | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                       |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 32.6 ms: 1.04x faster                                       |
| mako            | 6.56 ms                                                     | 6.35 ms: 1.03x faster                                       |
| django_template | 20.3 ms                                                     | 19.9 ms: 1.02x faster                                       |
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                       |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8                   | 23.8 ms                                                     | 15.0 ms: 1.59x faster                                       |
| pathlib                    | 75.3 ms                                                     | 61.8 ms: 1.22x faster                                       |
| regex_effbot               | 1.69 ms                                                     | 1.41 ms: 1.20x faster                                       |
| float                      | 50.8 ms                                                     | 47.7 ms: 1.07x faster                                       |
| json_dumps                 | 6.19 ms                                                     | 5.84 ms: 1.06x faster                                       |
| json                       | 3.30 ms                                                     | 3.12 ms: 1.06x faster                                       |
| thrift                     | 8.47 ms                                                     | 8.01 ms: 1.06x faster                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.46 ms: 1.06x faster                                       |
| async_generators           | 223 ms                                                      | 211 ms: 1.06x faster                                        |
| spectral_norm              | 63.4 ms                                                     | 60.4 ms: 1.05x faster                                       |
| generators                 | 19.0 ms                                                     | 18.2 ms: 1.04x faster                                       |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                       |
| genshi_xml                 | 33.9 ms                                                     | 32.6 ms: 1.04x faster                                       |
| mako                       | 6.56 ms                                                     | 6.35 ms: 1.03x faster                                       |
| chaos                      | 37.9 ms                                                     | 36.8 ms: 1.03x faster                                       |
| fannkuch                   | 252 ms                                                      | 245 ms: 1.03x faster                                        |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                       |
| nbody                      | 66.3 ms                                                     | 65.1 ms: 1.02x faster                                       |
| django_template            | 20.3 ms                                                     | 19.9 ms: 1.02x faster                                       |
| crypto_pyaes               | 45.6 ms                                                     | 44.8 ms: 1.02x faster                                       |
| sympy_expand               | 286 ms                                                      | 281 ms: 1.02x faster                                        |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.01x faster                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 277 ms: 1.01x faster                                        |
| gevent_hub                 | 0.67 ns                                                     | 0.66 ns: 1.01x faster                                       |
| hexiom                     | 3.84 ms                                                     | 3.79 ms: 1.01x faster                                       |
| regex_compile              | 80.7 ms                                                     | 79.8 ms: 1.01x faster                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.3 ms: 1.01x faster                                       |
| sqlglot_parse              | 764 us                                                      | 757 us: 1.01x faster                                        |
| xml_etree_parse            | 92.2 ms                                                     | 91.4 ms: 1.01x faster                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                        |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                       |
| sympy_str                  | 167 ms                                                      | 166 ms: 1.01x faster                                        |
| sqlglot_normalize          | 172 ms                                                      | 171 ms: 1.00x faster                                        |
| mdp                        | 1.43 sec                                                    | 1.43 sec: 1.00x faster                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.00x slower                                       |
| djangocms                  | 2.55 ms                                                     | 2.57 ms: 1.00x slower                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                        |
| docutils                   | 1.53 sec                                                    | 1.54 sec: 1.01x slower                                      |
| pprint_safe_repr           | 485 ms                                                      | 488 ms: 1.01x slower                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 32.8 ms: 1.01x slower                                       |
| go                         | 84.7 ms                                                     | 85.4 ms: 1.01x slower                                       |
| logging_silent             | 54.6 ns                                                     | 55.0 ns: 1.01x slower                                       |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                        |
| sympy_sum                  | 85.2 ms                                                     | 86.0 ms: 1.01x slower                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.90 sec: 1.01x slower                                      |
| deepcopy_memo              | 23.1 us                                                     | 23.3 us: 1.01x slower                                       |
| coverage                   | 45.3 ms                                                     | 45.8 ms: 1.01x slower                                       |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.01x slower                                       |
| scimark_sor                | 76.2 ms                                                     | 77.2 ms: 1.01x slower                                       |
| raytrace                   | 153 ms                                                      | 156 ms: 1.01x slower                                        |
| subparsers                 | 10.9 ms                                                     | 11.0 ms: 1.02x slower                                       |
| nqueens                    | 56.1 ms                                                     | 57.1 ms: 1.02x slower                                       |
| pprint_pformat             | 977 ms                                                      | 994 ms: 1.02x slower                                        |
| sqlalchemy_declarative     | 77.4 ms                                                     | 78.8 ms: 1.02x slower                                       |
| deepcopy                   | 223 us                                                      | 228 us: 1.02x slower                                        |
| pickle_pure_python         | 186 us                                                      | 189 us: 1.02x slower                                        |
| coroutines                 | 12.5 ms                                                     | 12.7 ms: 1.02x slower                                       |
| async_tree_none            | 219 ms                                                      | 224 ms: 1.02x slower                                        |
| sqlalchemy_imperative      | 9.30 ms                                                     | 9.52 ms: 1.02x slower                                       |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.03x slower                                      |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.03x slower                                       |
| bench_thread_pool          | 810 us                                                      | 831 us: 1.03x slower                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.26 ms: 1.03x slower                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.3 ms: 1.03x slower                                       |
| bench_mp_pool              | 84.2 ms                                                     | 86.6 ms: 1.03x slower                                       |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                       |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.09 us: 1.03x slower                                       |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                        |
| scimark_fft                | 175 ms                                                      | 183 ms: 1.05x slower                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 406 ms: 1.06x slower                                        |
| async_tree_io_tg           | 497 ms                                                      | 527 ms: 1.06x slower                                        |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                       |
| python_startup_no_site     | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                       |
| tornado_http               | 81.2 ms                                                     | 100 ms: 1.23x slower                                        |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                |

Benchmark hidden because not significant (24): pycparser, html5lib, meteor_contest, chameleon, connected_components, xml_etree_process, unpickle_pure_python, deltablue, tomli_loads, sqlglot_transpile, telco, many_optionals, logging_simple, async_tree_cpu_io_mixed, pyflate, typing_runtime_protocols, gc_traversal, xml_etree_generate, logging_format, async_tree_none_tg, async_tree_io, sphinx, async_tree_memoization, pylint

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 88.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown