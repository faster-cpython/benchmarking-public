# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization  | 453 ms                                                       | 326 ms: 1.39x faster                                                        |
| async_tree_io           | 843 ms                                                       | 615 ms: 1.37x faster                                                        |
| async_tree_none         | 376 ms                                                       | 285 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed | 604 ms                                                       | 504 ms: 1.20x faster                                                        |
| async_generators        | 457 ms                                                       | 446 ms: 1.02x faster                                                        |
| asyncio_websockets      | 388 ms                                                       | 385 ms: 1.01x faster                                                        |
| coroutines              | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                       |
| pidigits       | 252 ms                                                       | 257 ms: 1.02x slower                                                        |
| nbody          | 89.3 ms                                                      | 96.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.7 ms: 1.10x faster                                                       |
| regex_effbot   | 3.67 ms                                                      | 3.33 ms: 1.10x faster                                                       |
| regex_dna      | 247 ms                                                       | 227 ms: 1.09x faster                                                        |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 56.7 ms: 1.08x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 82.3 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.1 ms: 1.05x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 208 us: 1.04x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 330 us: 1.02x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 11.9 ms: 1.07x slower                                                       |
| json_loads           | 24.7 us                                                      | 26.5 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 13.6 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                                       |
| genshi_xml     | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                       |
| mako           | 10.4 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                      | 2.54 sec                                                     | 1.31 sec: 1.95x faster                                                      |
| deepcopy                 | 392 us                                                       | 274 us: 1.43x faster                                                        |
| richards                 | 52.9 ms                                                      | 37.4 ms: 1.42x faster                                                       |
| async_tree_memoization   | 453 ms                                                       | 326 ms: 1.39x faster                                                        |
| richards_super           | 59.6 ms                                                      | 42.8 ms: 1.39x faster                                                       |
| async_tree_io            | 843 ms                                                       | 615 ms: 1.37x faster                                                        |
| deepcopy_memo            | 38.6 us                                                      | 28.3 us: 1.37x faster                                                       |
| async_tree_none          | 376 ms                                                       | 285 ms: 1.32x faster                                                        |
| float                    | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                       |
| deepcopy_reduce          | 3.54 us                                                      | 2.90 us: 1.22x faster                                                       |
| tomli_loads              | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                      |
| async_tree_cpu_io_mixed  | 604 ms                                                       | 504 ms: 1.20x faster                                                        |
| scimark_sor              | 123 ms                                                       | 104 ms: 1.19x faster                                                        |
| generators               | 33.6 ms                                                      | 28.5 ms: 1.18x faster                                                       |
| go                       | 162 ms                                                       | 138 ms: 1.17x faster                                                        |
| python_startup           | 15.9 ms                                                      | 13.6 ms: 1.17x faster                                                       |
| deltablue                | 3.42 ms                                                      | 2.96 ms: 1.15x faster                                                       |
| dulwich_log              | 68.2 ms                                                      | 59.9 ms: 1.14x faster                                                       |
| genshi_text              | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                                       |
| html5lib                 | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                       |
| telco                    | 8.79 ms                                                      | 7.94 ms: 1.11x faster                                                       |
| pyflate                  | 503 ms                                                       | 456 ms: 1.10x faster                                                        |
| regex_v8                 | 26.1 ms                                                      | 23.7 ms: 1.10x faster                                                       |
| regex_effbot             | 3.67 ms                                                      | 3.33 ms: 1.10x faster                                                       |
| bpe_tokeniser            | 5.09 sec                                                     | 4.63 sec: 1.10x faster                                                      |
| xml_etree_parse          | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| regex_dna                | 247 ms                                                       | 227 ms: 1.09x faster                                                        |
| xml_etree_process        | 61.2 ms                                                      | 56.7 ms: 1.08x faster                                                       |
| pylint                   | 347 ms                                                       | 325 ms: 1.07x faster                                                        |
| spectral_norm            | 97.0 ms                                                      | 91.4 ms: 1.06x faster                                                       |
| genshi_xml               | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                       |
| regex_compile            | 143 ms                                                       | 135 ms: 1.06x faster                                                        |
| json                     | 5.69 ms                                                      | 5.38 ms: 1.06x faster                                                       |
| pprint_pformat           | 1.72 sec                                                     | 1.63 sec: 1.06x faster                                                      |
| xml_etree_generate       | 86.5 ms                                                      | 82.3 ms: 1.05x faster                                                       |
| sympy_integrate          | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 103 ms                                                       | 98.1 ms: 1.05x faster                                                       |
| unpickle_pure_python     | 217 us                                                       | 208 us: 1.04x faster                                                        |
| scimark_lu               | 98.7 ms                                                      | 94.7 ms: 1.04x faster                                                       |
| pprint_safe_repr         | 843 ms                                                       | 815 ms: 1.03x faster                                                        |
| thrift                   | 901 us                                                       | 877 us: 1.03x faster                                                        |
| scimark_fft              | 328 ms                                                       | 319 ms: 1.03x faster                                                        |
| 2to3                     | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| async_generators         | 457 ms                                                       | 446 ms: 1.02x faster                                                        |
| sympy_str                | 298 ms                                                       | 292 ms: 1.02x faster                                                        |
| python_startup_no_site   | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| pycparser                | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                      |
| sqlite_synth             | 2.91 us                                                      | 2.86 us: 1.02x faster                                                       |
| sympy_sum                | 155 ms                                                       | 152 ms: 1.01x faster                                                        |
| pathlib                  | 17.5 ms                                                      | 17.4 ms: 1.01x faster                                                       |
| sympy_expand             | 509 ms                                                       | 505 ms: 1.01x faster                                                        |
| asyncio_websockets       | 388 ms                                                       | 385 ms: 1.01x faster                                                        |
| coverage                 | 80.0 ms                                                      | 79.6 ms: 1.00x faster                                                       |
| mako                     | 10.4 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| scimark_monte_carlo      | 66.1 ms                                                      | 66.7 ms: 1.01x slower                                                       |
| logging_simple           | 6.39 us                                                      | 6.49 us: 1.02x slower                                                       |
| pidigits                 | 252 ms                                                       | 257 ms: 1.02x slower                                                        |
| chaos                    | 60.2 ms                                                      | 61.4 ms: 1.02x slower                                                       |
| nqueens                  | 90.7 ms                                                      | 92.7 ms: 1.02x slower                                                       |
| pickle_pure_python       | 323 us                                                       | 330 us: 1.02x slower                                                        |
| logging_format           | 6.94 us                                                      | 7.14 us: 1.03x slower                                                       |
| meteor_contest           | 130 ms                                                       | 134 ms: 1.03x slower                                                        |
| coroutines               | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| docutils                 | 2.83 sec                                                     | 2.93 sec: 1.04x slower                                                      |
| typing_runtime_protocols | 169 us                                                       | 177 us: 1.04x slower                                                        |
| bench_thread_pool        | 942 us                                                       | 988 us: 1.05x slower                                                        |
| scimark_sparse_mat_mult  | 4.77 ms                                                      | 5.01 ms: 1.05x slower                                                       |
| create_gc_cycles         | 2.68 ms                                                      | 2.81 ms: 1.05x slower                                                       |
| raytrace                 | 273 ms                                                       | 288 ms: 1.06x slower                                                        |
| json_dumps               | 11.1 ms                                                      | 11.9 ms: 1.07x slower                                                       |
| json_loads               | 24.7 us                                                      | 26.5 us: 1.07x slower                                                       |
| nbody                    | 89.3 ms                                                      | 96.5 ms: 1.08x slower                                                       |
| crypto_pyaes             | 73.3 ms                                                      | 80.4 ms: 1.10x slower                                                       |
| many_optionals           | 930 us                                                       | 1.04 ms: 1.12x slower                                                       |
| comprehensions           | 17.0 us                                                      | 19.2 us: 1.13x slower                                                       |
| fannkuch                 | 363 ms                                                       | 412 ms: 1.13x slower                                                        |
| gc_traversal             | 4.74 ms                                                      | 6.47 ms: 1.37x slower                                                       |
| subparsers               | 17.5 ms                                                      | 24.2 ms: 1.38x slower                                                       |
| logging_silent           | 97.9 ns                                                      | 507 ns: 5.18x slower                                                        |
| bench_mp_pool            | 5.12 ms                                                      | 1.28 sec: 250.64x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (3): djangocms, django_template, hexiom
Ignored benchmarks (18) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x