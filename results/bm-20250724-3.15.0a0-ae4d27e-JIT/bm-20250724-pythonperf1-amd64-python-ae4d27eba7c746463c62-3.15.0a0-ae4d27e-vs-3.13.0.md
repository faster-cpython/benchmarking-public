# Results vs. 3.13.0

- fork: python
- ref: ae4d27eba7c746463c62
- machine: windows-amd64
- commit hash: ae4d27e
- commit date: 2025-07-24
- overall geometric mean: 1.063x faster
- HPT reliability: 76.46%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                      |
| sphinx         | 617 ms                                                      | 647 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.26x faster                                                       |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 338 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 55.7 ms: 1.19x faster                                                      |
| float          | 50.8 ms                                                     | 45.6 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 81.4 ms: 1.01x slower                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 106 us: 1.23x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.13 sec: 1.22x faster                                                     |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 52.4 ms: 1.02x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 94.6 ms: 1.03x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.39 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 67.0 ms: 1.11x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.7 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.48 ms: 1.20x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 36.6 ms: 1.08x slower                                                      |
| django_template | 20.3 ms                                                     | 24.5 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 495 us: 17.10x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.9 ms: 2.29x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| mdp                        | 1.43 sec                                                    | 815 ms: 1.76x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                      |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                       |
| deepcopy                   | 223 us                                                      | 176 us: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.26x faster                                                       |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.23x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.13 sec: 1.22x faster                                                     |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.2 us: 1.20x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.48 ms: 1.20x faster                                                      |
| nbody                      | 66.3 ms                                                     | 55.7 ms: 1.19x faster                                                      |
| fannkuch                   | 252 ms                                                      | 213 ms: 1.18x faster                                                       |
| scimark_fft                | 175 ms                                                      | 151 ms: 1.15x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.22 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.28 ms: 1.14x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.52 sec: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 338 ms: 1.12x faster                                                       |
| float                      | 50.8 ms                                                     | 45.6 ms: 1.11x faster                                                      |
| pyflate                    | 283 ms                                                      | 255 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 348 ms: 1.10x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 896 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 446 ms: 1.09x faster                                                       |
| json                       | 3.30 ms                                                     | 3.07 ms: 1.07x faster                                                      |
| go                         | 84.7 ms                                                     | 79.0 ms: 1.07x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.92 us: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 52.4 ms: 1.02x faster                                                      |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 45.9 ms: 1.01x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 81.4 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 94.6 ms: 1.03x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.03x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.39 ms: 1.03x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 65.5 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 88.0 ms: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 79.4 ms: 1.04x slower                                                      |
| sympy_expand               | 286 ms                                                      | 298 ms: 1.04x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.2 ms: 1.05x slower                                                      |
| sphinx                     | 617 ms                                                      | 647 ms: 1.05x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.3 ns: 1.05x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.3 ms: 1.05x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.9 ms: 1.06x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.8 ms: 1.07x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 36.6 ms: 1.08x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                     |
| coverage                   | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.7 ms: 1.09x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.78 us: 1.10x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 67.0 ms: 1.11x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.40 us: 1.11x slower                                                      |
| chaos                      | 37.9 ms                                                     | 42.1 ms: 1.11x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.28 ms: 1.11x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.37 ms: 1.12x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 62.7 ms: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.18x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| raytrace                   | 153 ms                                                      | 184 ms: 1.20x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.5 ms: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 598 us: 1.66x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.9 ms: 2.94x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (7): pylint, meteor_contest, scimark_monte_carlo, xml_etree_process, pidigits, typing_runtime_protocols, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250724-3.15.0a0-ae4d27e-JIT/bm-20250724-pythonperf1-amd64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 76.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown