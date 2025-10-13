# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.6 ms: 1.10x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                        |
| async_tree_none            | 376 ms                                                       | 272 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 629 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 512 ms: 1.14x faster                                                        |
| async_generators           | 457 ms                                                       | 442 ms: 1.03x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 67.8 ms: 1.20x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 103 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.30 ms: 1.11x faster                                                       |
| regex_dna      | 247 ms                                                       | 225 ms: 1.10x faster                                                        |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.2 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.90 sec: 1.29x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 194 us: 1.12x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 10.1 ms: 1.11x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 55.5 ms: 1.10x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 80.1 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 96.5 ms: 1.07x faster                                                       |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 329 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                       |
| mako            | 10.4 ms                                                      | 9.85 ms: 1.05x faster                                                       |
| django_template | 36.4 ms                                                      | 34.9 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 2.01x faster                                                      |
| deepcopy                   | 392 us                                                       | 262 us: 1.49x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 26.2 us: 1.47x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                        |
| async_tree_none            | 376 ms                                                       | 272 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 616 ms: 1.37x faster                                                        |
| go                         | 162 ms                                                       | 119 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 629 ms: 1.32x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.90 sec: 1.29x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                        |
| pyflate                    | 503 ms                                                       | 395 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.87 us: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| scimark_fft                | 328 ms                                                       | 273 ms: 1.20x faster                                                        |
| float                      | 81.3 ms                                                      | 67.8 ms: 1.20x faster                                                       |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.19x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.47 sec: 1.17x faster                                                      |
| richards                   | 52.9 ms                                                      | 45.3 ms: 1.17x faster                                                       |
| richards_super             | 59.6 ms                                                      | 51.3 ms: 1.16x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 727 ms: 1.16x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.2 ms: 1.15x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 59.6 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 512 ms: 1.14x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 86.2 ms: 1.13x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 194 us: 1.12x faster                                                        |
| generators                 | 33.6 ms                                                      | 30.1 ms: 1.12x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.58 sec: 1.11x faster                                                      |
| regex_effbot               | 3.67 ms                                                      | 3.30 ms: 1.11x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 10.1 ms: 1.11x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.94 ms: 1.10x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 66.6 ms: 1.10x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 55.5 ms: 1.10x faster                                                       |
| regex_dna                  | 247 ms                                                       | 225 ms: 1.10x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.89 us: 1.09x faster                                                       |
| pylint                     | 347 ms                                                       | 320 ms: 1.08x faster                                                        |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.2 ms: 1.08x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 80.1 ms: 1.08x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                      |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.19 ms: 1.07x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.49 us: 1.07x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 96.5 ms: 1.07x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.2 ms: 1.06x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 92.4 ns: 1.06x faster                                                       |
| thrift                     | 901 us                                                       | 851 us: 1.06x faster                                                        |
| connected_components       | 432 ms                                                       | 409 ms: 1.06x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.85 ms: 1.05x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.77 us: 1.05x faster                                                       |
| json                       | 5.69 ms                                                      | 5.44 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 94.6 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| django_template            | 36.4 ms                                                      | 34.9 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                        |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.9 ms: 1.03x faster                                                       |
| async_generators           | 457 ms                                                       | 442 ms: 1.03x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.20 sec: 1.03x faster                                                      |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| chaos                      | 60.2 ms                                                      | 58.4 ms: 1.03x faster                                                       |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.03x faster                                                        |
| sympy_expand               | 509 ms                                                       | 502 ms: 1.01x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                        |
| coverage                   | 80.0 ms                                                      | 80.3 ms: 1.00x slower                                                       |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 92.0 ms: 1.01x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 329 us: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| raytrace                   | 273 ms                                                       | 280 ms: 1.03x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 76.9 ms: 1.05x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.90 ms: 1.08x slower                                                       |
| nbody                      | 89.3 ms                                                      | 103 ms: 1.15x slower                                                        |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.51 ms: 1.37x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 44.6 ms: 2.55x slower                                                       |
| telco                      | 8.79 ms                                                      | 154 ms: 17.48x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 2.57 sec: 500.80x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, djangocms, fannkuch, scimark_sparse_mat_mult
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x