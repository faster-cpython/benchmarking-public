# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization  | 453 ms                                                       | 329 ms: 1.38x faster                                                        |
| async_tree_io           | 843 ms                                                       | 629 ms: 1.34x faster                                                        |
| async_tree_none         | 376 ms                                                       | 286 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed | 604 ms                                                       | 503 ms: 1.20x faster                                                        |
| async_generators        | 457 ms                                                       | 429 ms: 1.07x faster                                                        |
| coroutines              | 21.6 ms                                                      | 22.1 ms: 1.03x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.17x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.1 ms: 1.16x faster                                                       |
| pidigits       | 252 ms                                                       | 257 ms: 1.02x slower                                                        |
| nbody          | 89.3 ms                                                      | 95.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.43 ms: 1.07x faster                                                       |
| regex_compile  | 143 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                                       |
| regex_dna      | 247 ms                                                       | 240 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.09 sec: 1.18x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 141 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 98.2 ms: 1.05x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 58.8 ms: 1.04x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 85.0 ms: 1.02x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 215 us: 1.01x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 330 us: 1.02x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 11.9 ms: 1.06x slower                                                       |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 13.6 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.77 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.3 ms: 1.07x faster                                                       |
| django_template | 36.4 ms                                                      | 35.8 ms: 1.02x faster                                                       |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                      | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                      |
| deepcopy                 | 392 us                                                       | 278 us: 1.41x faster                                                        |
| deepcopy_memo            | 38.6 us                                                      | 27.6 us: 1.40x faster                                                       |
| async_tree_memoization   | 453 ms                                                       | 329 ms: 1.38x faster                                                        |
| async_tree_io            | 843 ms                                                       | 629 ms: 1.34x faster                                                        |
| async_tree_none          | 376 ms                                                       | 286 ms: 1.31x faster                                                        |
| go                       | 162 ms                                                       | 125 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed  | 604 ms                                                       | 503 ms: 1.20x faster                                                        |
| deepcopy_reduce          | 3.54 us                                                      | 2.96 us: 1.20x faster                                                       |
| generators               | 33.6 ms                                                      | 28.3 ms: 1.19x faster                                                       |
| tomli_loads              | 2.46 sec                                                     | 2.09 sec: 1.18x faster                                                      |
| richards                 | 52.9 ms                                                      | 44.9 ms: 1.18x faster                                                       |
| python_startup           | 15.9 ms                                                      | 13.6 ms: 1.17x faster                                                       |
| scimark_sor              | 123 ms                                                       | 105 ms: 1.17x faster                                                        |
| richards_super           | 59.6 ms                                                      | 51.1 ms: 1.17x faster                                                       |
| float                    | 81.3 ms                                                      | 70.1 ms: 1.16x faster                                                       |
| dulwich_log              | 68.2 ms                                                      | 60.0 ms: 1.14x faster                                                       |
| genshi_text              | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                       |
| pyflate                  | 503 ms                                                       | 452 ms: 1.11x faster                                                        |
| telco                    | 8.79 ms                                                      | 7.91 ms: 1.11x faster                                                       |
| html5lib                 | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                       |
| scimark_monte_carlo      | 66.1 ms                                                      | 60.0 ms: 1.10x faster                                                       |
| deltablue                | 3.42 ms                                                      | 3.13 ms: 1.09x faster                                                       |
| bpe_tokeniser            | 5.09 sec                                                     | 4.68 sec: 1.09x faster                                                      |
| pprint_pformat           | 1.72 sec                                                     | 1.59 sec: 1.08x faster                                                      |
| pprint_safe_repr         | 843 ms                                                       | 782 ms: 1.08x faster                                                        |
| hexiom                   | 6.55 ms                                                      | 6.08 ms: 1.08x faster                                                       |
| pylint                   | 347 ms                                                       | 324 ms: 1.07x faster                                                        |
| genshi_xml               | 57.1 ms                                                      | 53.3 ms: 1.07x faster                                                       |
| regex_effbot             | 3.67 ms                                                      | 3.43 ms: 1.07x faster                                                       |
| xml_etree_parse          | 150 ms                                                       | 141 ms: 1.07x faster                                                        |
| sympy_integrate          | 23.6 ms                                                      | 22.1 ms: 1.07x faster                                                       |
| async_generators         | 457 ms                                                       | 429 ms: 1.07x faster                                                        |
| regex_compile            | 143 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_v8                 | 26.1 ms                                                      | 24.6 ms: 1.06x faster                                                       |
| thrift                   | 901 us                                                       | 851 us: 1.06x faster                                                        |
| json                     | 5.69 ms                                                      | 5.39 ms: 1.05x faster                                                       |
| scimark_fft              | 328 ms                                                       | 313 ms: 1.05x faster                                                        |
| spectral_norm            | 97.0 ms                                                      | 92.6 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 103 ms                                                       | 98.2 ms: 1.05x faster                                                       |
| 2to3                     | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| xml_etree_process        | 61.2 ms                                                      | 58.8 ms: 1.04x faster                                                       |
| scimark_lu               | 98.7 ms                                                      | 95.2 ms: 1.04x faster                                                       |
| sympy_str                | 298 ms                                                       | 289 ms: 1.03x faster                                                        |
| regex_dna                | 247 ms                                                       | 240 ms: 1.03x faster                                                        |
| sympy_expand             | 509 ms                                                       | 497 ms: 1.03x faster                                                        |
| python_startup_no_site   | 8.96 ms                                                      | 8.77 ms: 1.02x faster                                                       |
| xml_etree_generate       | 86.5 ms                                                      | 85.0 ms: 1.02x faster                                                       |
| sympy_sum                | 155 ms                                                       | 152 ms: 1.02x faster                                                        |
| django_template          | 36.4 ms                                                      | 35.8 ms: 1.02x faster                                                       |
| meteor_contest           | 130 ms                                                       | 128 ms: 1.01x faster                                                        |
| unpickle_pure_python     | 217 us                                                       | 215 us: 1.01x faster                                                        |
| pathlib                  | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult  | 4.77 ms                                                      | 4.75 ms: 1.01x faster                                                       |
| chaos                    | 60.2 ms                                                      | 60.0 ms: 1.00x faster                                                       |
| comprehensions           | 17.0 us                                                      | 17.1 us: 1.00x slower                                                       |
| typing_runtime_protocols | 169 us                                                       | 171 us: 1.01x slower                                                        |
| fannkuch                 | 363 ms                                                       | 369 ms: 1.02x slower                                                        |
| nqueens                  | 90.7 ms                                                      | 92.2 ms: 1.02x slower                                                       |
| docutils                 | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                      |
| pidigits                 | 252 ms                                                       | 257 ms: 1.02x slower                                                        |
| pycparser                | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                                      |
| pickle_pure_python       | 323 us                                                       | 330 us: 1.02x slower                                                        |
| coroutines               | 21.6 ms                                                      | 22.1 ms: 1.03x slower                                                       |
| logging_format           | 6.94 us                                                      | 7.13 us: 1.03x slower                                                       |
| logging_simple           | 6.39 us                                                      | 6.59 us: 1.03x slower                                                       |
| raytrace                 | 273 ms                                                       | 282 ms: 1.04x slower                                                        |
| mako                     | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| create_gc_cycles         | 2.68 ms                                                      | 2.80 ms: 1.04x slower                                                       |
| bench_thread_pool        | 942 us                                                       | 986 us: 1.05x slower                                                        |
| coverage                 | 80.0 ms                                                      | 84.6 ms: 1.06x slower                                                       |
| nbody                    | 89.3 ms                                                      | 95.1 ms: 1.06x slower                                                       |
| json_dumps               | 11.1 ms                                                      | 11.9 ms: 1.06x slower                                                       |
| json_loads               | 24.7 us                                                      | 26.4 us: 1.07x slower                                                       |
| crypto_pyaes             | 73.3 ms                                                      | 79.8 ms: 1.09x slower                                                       |
| many_optionals           | 930 us                                                       | 1.02 ms: 1.10x slower                                                       |
| gc_traversal             | 4.74 ms                                                      | 6.42 ms: 1.35x slower                                                       |
| subparsers               | 17.5 ms                                                      | 24.3 ms: 1.39x slower                                                       |
| logging_silent           | 97.9 ns                                                      | 517 ns: 5.28x slower                                                        |
| bench_mp_pool            | 5.12 ms                                                      | 1.32 sec: 257.94x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (3): sqlite_synth, djangocms, asyncio_websockets
Ignored benchmarks (18) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x