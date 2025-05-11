# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.034x slower
- HPT reliability: 97.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 317 ms: 1.08x slower                                                        |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 843 ms                                                       | 560 ms: 1.51x faster                                                        |
| async_tree_none         | 376 ms                                                       | 265 ms: 1.42x faster                                                        |
| async_tree_memoization  | 453 ms                                                       | 321 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| asyncio_websockets      | 388 ms                                                       | 379 ms: 1.02x faster                                                        |
| coroutines              | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                       |
| async_generators        | 457 ms                                                       | 484 ms: 1.06x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.6 ms: 1.14x faster                                                       |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                        |
| nbody          | 89.3 ms                                                      | 128 ms: 1.43x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.8 ms: 1.10x faster                                                       |
| regex_effbot   | 3.67 ms                                                      | 3.37 ms: 1.09x faster                                                       |
| regex_dna      | 247 ms                                                       | 236 ms: 1.05x faster                                                        |
| regex_compile  | 143 ms                                                       | 156 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.4 ms: 1.16x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.28 sec: 1.08x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 234 us: 1.07x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 359 us: 1.11x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 69.9 ms: 1.14x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 99.6 ms: 1.15x slower                                                       |
| json_loads           | 24.7 us                                                      | 29.1 us: 1.18x slower                                                       |
| json_dumps           | 11.1 ms                                                      | 13.7 ms: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 17.7 ms: 1.11x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 61.6 ms: 1.08x slower                                                       |
| genshi_text     | 26.2 ms                                                      | 29.4 ms: 1.12x slower                                                       |
| django_template | 36.4 ms                                                      | 42.6 ms: 1.17x slower                                                       |
| mako            | 10.4 ms                                                      | 17.4 ms: 1.67x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.24x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal             | 4.74 ms                                                      | 2.22 ms: 2.14x faster                                                       |
| mdp                      | 2.54 sec                                                     | 1.49 sec: 1.71x faster                                                      |
| async_tree_io            | 843 ms                                                       | 560 ms: 1.51x faster                                                        |
| async_tree_none          | 376 ms                                                       | 265 ms: 1.42x faster                                                        |
| async_tree_memoization   | 453 ms                                                       | 321 ms: 1.41x faster                                                        |
| create_gc_cycles         | 2.68 ms                                                      | 2.04 ms: 1.32x faster                                                       |
| deepcopy                 | 392 us                                                       | 319 us: 1.23x faster                                                        |
| async_tree_cpu_io_mixed  | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| xml_etree_iterparse      | 103 ms                                                       | 88.4 ms: 1.16x faster                                                       |
| float                    | 81.3 ms                                                      | 71.6 ms: 1.14x faster                                                       |
| deepcopy_memo            | 38.6 us                                                      | 34.1 us: 1.13x faster                                                       |
| go                       | 162 ms                                                       | 143 ms: 1.13x faster                                                        |
| sqlite_synth             | 2.91 us                                                      | 2.65 us: 1.10x faster                                                       |
| regex_v8                 | 26.1 ms                                                      | 23.8 ms: 1.10x faster                                                       |
| xml_etree_parse          | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| regex_effbot             | 3.67 ms                                                      | 3.37 ms: 1.09x faster                                                       |
| dulwich_log              | 68.2 ms                                                      | 62.7 ms: 1.09x faster                                                       |
| tomli_loads              | 2.46 sec                                                     | 2.28 sec: 1.08x faster                                                      |
| pyflate                  | 503 ms                                                       | 475 ms: 1.06x faster                                                        |
| scimark_sor              | 123 ms                                                       | 117 ms: 1.05x faster                                                        |
| html5lib                 | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                       |
| regex_dna                | 247 ms                                                       | 236 ms: 1.05x faster                                                        |
| generators               | 33.6 ms                                                      | 32.2 ms: 1.04x faster                                                       |
| deepcopy_reduce          | 3.54 us                                                      | 3.42 us: 1.03x faster                                                       |
| asyncio_websockets       | 388 ms                                                       | 379 ms: 1.02x faster                                                        |
| pathlib                  | 17.5 ms                                                      | 17.3 ms: 1.02x faster                                                       |
| bpe_tokeniser            | 5.09 sec                                                     | 5.04 sec: 1.01x faster                                                      |
| pidigits                 | 252 ms                                                       | 252 ms: 1.00x faster                                                        |
| pycparser                | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                      |
| coroutines               | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                       |
| richards                 | 52.9 ms                                                      | 54.2 ms: 1.02x slower                                                       |
| docutils                 | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| hexiom                   | 6.55 ms                                                      | 6.83 ms: 1.04x slower                                                       |
| richards_super           | 59.6 ms                                                      | 62.2 ms: 1.04x slower                                                       |
| telco                    | 8.79 ms                                                      | 9.20 ms: 1.05x slower                                                       |
| spectral_norm            | 97.0 ms                                                      | 103 ms: 1.06x slower                                                        |
| pprint_safe_repr         | 843 ms                                                       | 893 ms: 1.06x slower                                                        |
| async_generators         | 457 ms                                                       | 484 ms: 1.06x slower                                                        |
| pprint_pformat           | 1.72 sec                                                     | 1.84 sec: 1.07x slower                                                      |
| deltablue                | 3.42 ms                                                      | 3.65 ms: 1.07x slower                                                       |
| unpickle_pure_python     | 217 us                                                       | 234 us: 1.07x slower                                                        |
| sympy_integrate          | 23.6 ms                                                      | 25.4 ms: 1.08x slower                                                       |
| genshi_xml               | 57.1 ms                                                      | 61.6 ms: 1.08x slower                                                       |
| 2to3                     | 293 ms                                                       | 317 ms: 1.08x slower                                                        |
| scimark_fft              | 328 ms                                                       | 356 ms: 1.08x slower                                                        |
| regex_compile            | 143 ms                                                       | 156 ms: 1.09x slower                                                        |
| sympy_expand             | 509 ms                                                       | 559 ms: 1.10x slower                                                        |
| sympy_str                | 298 ms                                                       | 328 ms: 1.10x slower                                                        |
| thrift                   | 901 us                                                       | 995 us: 1.11x slower                                                        |
| pickle_pure_python       | 323 us                                                       | 359 us: 1.11x slower                                                        |
| python_startup           | 15.9 ms                                                      | 17.7 ms: 1.11x slower                                                       |
| sympy_sum                | 155 ms                                                       | 172 ms: 1.11x slower                                                        |
| chaos                    | 60.2 ms                                                      | 67.4 ms: 1.12x slower                                                       |
| genshi_text              | 26.2 ms                                                      | 29.4 ms: 1.12x slower                                                       |
| scimark_lu               | 98.7 ms                                                      | 111 ms: 1.12x slower                                                        |
| xml_etree_process        | 61.2 ms                                                      | 69.9 ms: 1.14x slower                                                       |
| nqueens                  | 90.7 ms                                                      | 104 ms: 1.14x slower                                                        |
| xml_etree_generate       | 86.5 ms                                                      | 99.6 ms: 1.15x slower                                                       |
| logging_simple           | 6.39 us                                                      | 7.41 us: 1.16x slower                                                       |
| many_optionals           | 930 us                                                       | 1.08 ms: 1.16x slower                                                       |
| django_template          | 36.4 ms                                                      | 42.6 ms: 1.17x slower                                                       |
| json_loads               | 24.7 us                                                      | 29.1 us: 1.18x slower                                                       |
| logging_format           | 6.94 us                                                      | 8.21 us: 1.18x slower                                                       |
| raytrace                 | 273 ms                                                       | 323 ms: 1.19x slower                                                        |
| comprehensions           | 17.0 us                                                      | 20.2 us: 1.19x slower                                                       |
| meteor_contest           | 130 ms                                                       | 154 ms: 1.19x slower                                                        |
| json_dumps               | 11.1 ms                                                      | 13.7 ms: 1.23x slower                                                       |
| scimark_monte_carlo      | 66.1 ms                                                      | 81.9 ms: 1.24x slower                                                       |
| scimark_sparse_mat_mult  | 4.77 ms                                                      | 5.93 ms: 1.24x slower                                                       |
| fannkuch                 | 363 ms                                                       | 463 ms: 1.27x slower                                                        |
| typing_runtime_protocols | 169 us                                                       | 218 us: 1.29x slower                                                        |
| crypto_pyaes             | 73.3 ms                                                      | 94.8 ms: 1.29x slower                                                       |
| python_startup_no_site   | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                       |
| nbody                    | 89.3 ms                                                      | 128 ms: 1.43x slower                                                        |
| bench_thread_pool        | 942 us                                                       | 1.42 ms: 1.51x slower                                                       |
| subparsers               | 17.5 ms                                                      | 26.7 ms: 1.53x slower                                                       |
| coverage                 | 80.0 ms                                                      | 122 ms: 1.53x slower                                                        |
| mako                     | 10.4 ms                                                      | 17.4 ms: 1.67x slower                                                       |
| logging_silent           | 97.9 ns                                                      | 608 ns: 6.22x slower                                                        |
| bench_mp_pool            | 5.12 ms                                                      | 57.1 ms: 11.15x slower                                                      |
| Geometric mean           | (ref)                                                        | 1.09x slower                                                                |

Benchmark hidden because not significant (2): json, pylint
Ignored benchmarks (19) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, djangocms, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 97.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.30x