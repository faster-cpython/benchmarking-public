# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.2 ms: 1.11x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.41x faster                                                        |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 64.3 ms: 1.26x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 103 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.0 ms: 1.13x faster                                                       |
| regex_dna      | 247 ms                                                       | 223 ms: 1.11x faster                                                        |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.57 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 197 us: 1.10x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 55.6 ms: 1.10x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 79.2 ms: 1.09x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 96.7 ms: 1.06x faster                                                       |
| json_dumps           | 11.1 ms                                                      | 11.2 ms: 1.01x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 333 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.71 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.1 ms: 1.14x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.9 ms: 1.06x faster                                                       |
| mako            | 10.4 ms                                                      | 9.96 ms: 1.04x faster                                                       |
| django_template | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.28 sec: 1.98x faster                                                      |
| richards                   | 52.9 ms                                                      | 34.9 ms: 1.52x faster                                                       |
| richards_super             | 59.6 ms                                                      | 41.1 ms: 1.45x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.41x faster                                                        |
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 28.0 us: 1.38x faster                                                       |
| async_tree_none            | 376 ms                                                       | 274 ms: 1.37x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                      |
| go                         | 162 ms                                                       | 127 ms: 1.27x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                        |
| float                      | 81.3 ms                                                      | 64.3 ms: 1.26x faster                                                       |
| pyflate                    | 503 ms                                                       | 411 ms: 1.22x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 80.6 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| scimark_sor                | 123 ms                                                       | 105 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.01 us: 1.18x faster                                                       |
| deltablue                  | 3.42 ms                                                      | 2.91 ms: 1.17x faster                                                       |
| generators                 | 33.6 ms                                                      | 29.2 ms: 1.15x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 59.2 ms: 1.15x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.49 sec: 1.15x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 737 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.1 ms: 1.14x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.0 ms: 1.13x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 66.2 ms: 1.11x faster                                                       |
| regex_dna                  | 247 ms                                                       | 223 ms: 1.11x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.61 sec: 1.10x faster                                                      |
| unpickle_pure_python       | 217 us                                                       | 197 us: 1.10x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 55.6 ms: 1.10x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 79.2 ms: 1.09x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                      |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                        |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                        |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                        |
| json                       | 5.69 ms                                                      | 5.35 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 96.7 ms: 1.06x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.18 ms: 1.06x faster                                                       |
| connected_components       | 432 ms                                                       | 408 ms: 1.06x faster                                                        |
| thrift                     | 901 us                                                       | 850 us: 1.06x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 53.9 ms: 1.06x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.61 us: 1.05x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.5 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.3 ms: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                       |
| logging_simple             | 6.39 us                                                      | 6.12 us: 1.04x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 93.8 ns: 1.04x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.96 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 17.0 ms: 1.03x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.57 ms: 1.03x faster                                                       |
| sympy_expand               | 509 ms                                                       | 495 ms: 1.03x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.71 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                       |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 96.7 ms: 1.02x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                        |
| chaos                      | 60.2 ms                                                      | 60.5 ms: 1.01x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.2 ms: 1.01x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                      |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.2 us: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 92.5 ms: 1.02x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 333 us: 1.03x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| coverage                   | 80.0 ms                                                      | 83.7 ms: 1.05x slower                                                       |
| fannkuch                   | 363 ms                                                       | 380 ms: 1.05x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 77.1 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.04 ms: 1.06x slower                                                       |
| bench_thread_pool          | 942 us                                                       | 1.00 ms: 1.06x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.86 ms: 1.07x slower                                                       |
| raytrace                   | 273 ms                                                       | 293 ms: 1.07x slower                                                        |
| many_optionals             | 930 us                                                       | 1.05 ms: 1.13x slower                                                       |
| nbody                      | 89.3 ms                                                      | 103 ms: 1.15x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.47 ms: 1.36x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 25.0 ms: 1.43x slower                                                       |
| telco                      | 8.79 ms                                                      | 161 ms: 18.34x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.51 sec: 294.92x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (2): djangocms, async_generators
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x