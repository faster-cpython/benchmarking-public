# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 279 ms: 1.05x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                      |
| html5lib       | 73.5 ms                                                      | 65.6 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization  | 453 ms                                                       | 313 ms: 1.45x faster                                                        |
| async_tree_io           | 843 ms                                                       | 604 ms: 1.40x faster                                                        |
| async_tree_none         | 376 ms                                                       | 272 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed | 604 ms                                                       | 518 ms: 1.16x faster                                                        |
| coroutines              | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                       |
| async_generators        | 457 ms                                                       | 447 ms: 1.02x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.19x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 65.8 ms: 1.24x faster                                                       |
| nbody          | 89.3 ms                                                      | 94.6 ms: 1.06x slower                                                       |
| pidigits       | 252 ms                                                       | 292 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.52 ms: 1.04x faster                                                       |
| regex_dna      | 247 ms                                                       | 242 ms: 1.02x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 28.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.01 sec: 1.23x faster                                                      |
| xml_etree_process    | 61.2 ms                                                      | 56.3 ms: 1.09x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 80.0 ms: 1.08x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 202 us: 1.08x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 313 us: 1.03x faster                                                        |
| json_loads           | 24.7 us                                                      | 26.3 us: 1.07x slower                                                       |
| json_dumps           | 11.1 ms                                                      | 12.0 ms: 1.08x slower                                                       |
| xml_etree_parse      | 150 ms                                                       | 167 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 13.7 ms: 1.16x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.90 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.1 ms: 1.18x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 52.2 ms: 1.09x faster                                                       |
| django_template | 36.4 ms                                                      | 34.4 ms: 1.06x faster                                                       |
| mako            | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                      | 2.54 sec                                                     | 1.27 sec: 1.99x faster                                                      |
| deepcopy                 | 392 us                                                       | 257 us: 1.53x faster                                                        |
| deepcopy_memo            | 38.6 us                                                      | 26.2 us: 1.47x faster                                                       |
| async_tree_memoization   | 453 ms                                                       | 313 ms: 1.45x faster                                                        |
| async_tree_io            | 843 ms                                                       | 604 ms: 1.40x faster                                                        |
| async_tree_none          | 376 ms                                                       | 272 ms: 1.38x faster                                                        |
| scimark_sor              | 123 ms                                                       | 91.5 ms: 1.35x faster                                                       |
| go                       | 162 ms                                                       | 121 ms: 1.34x faster                                                        |
| deepcopy_reduce          | 3.54 us                                                      | 2.70 us: 1.31x faster                                                       |
| richards                 | 52.9 ms                                                      | 42.3 ms: 1.25x faster                                                       |
| pyflate                  | 503 ms                                                       | 405 ms: 1.24x faster                                                        |
| float                    | 81.3 ms                                                      | 65.8 ms: 1.24x faster                                                       |
| richards_super           | 59.6 ms                                                      | 48.5 ms: 1.23x faster                                                       |
| tomli_loads              | 2.46 sec                                                     | 2.01 sec: 1.23x faster                                                      |
| telco                    | 8.79 ms                                                      | 7.30 ms: 1.20x faster                                                       |
| genshi_text              | 26.2 ms                                                      | 22.1 ms: 1.18x faster                                                       |
| scimark_fft              | 328 ms                                                       | 279 ms: 1.17x faster                                                        |
| hexiom                   | 6.55 ms                                                      | 5.62 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed  | 604 ms                                                       | 518 ms: 1.16x faster                                                        |
| python_startup           | 15.9 ms                                                      | 13.7 ms: 1.16x faster                                                       |
| dulwich_log              | 68.2 ms                                                      | 58.9 ms: 1.16x faster                                                       |
| scimark_monte_carlo      | 66.1 ms                                                      | 57.5 ms: 1.15x faster                                                       |
| spectral_norm            | 97.0 ms                                                      | 86.0 ms: 1.13x faster                                                       |
| html5lib                 | 73.5 ms                                                      | 65.6 ms: 1.12x faster                                                       |
| scimark_lu               | 98.7 ms                                                      | 88.1 ms: 1.12x faster                                                       |
| deltablue                | 3.42 ms                                                      | 3.05 ms: 1.12x faster                                                       |
| pprint_pformat           | 1.72 sec                                                     | 1.54 sec: 1.11x faster                                                      |
| thrift                   | 901 us                                                       | 809 us: 1.11x faster                                                        |
| scimark_sparse_mat_mult  | 4.77 ms                                                      | 4.30 ms: 1.11x faster                                                       |
| pprint_safe_repr         | 843 ms                                                       | 758 ms: 1.11x faster                                                        |
| generators               | 33.6 ms                                                      | 30.4 ms: 1.11x faster                                                       |
| bpe_tokeniser            | 5.09 sec                                                     | 4.60 sec: 1.11x faster                                                      |
| pylint                   | 347 ms                                                       | 317 ms: 1.09x faster                                                        |
| genshi_xml               | 57.1 ms                                                      | 52.2 ms: 1.09x faster                                                       |
| regex_compile            | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| xml_etree_process        | 61.2 ms                                                      | 56.3 ms: 1.09x faster                                                       |
| xml_etree_generate       | 86.5 ms                                                      | 80.0 ms: 1.08x faster                                                       |
| sympy_integrate          | 23.6 ms                                                      | 21.8 ms: 1.08x faster                                                       |
| raytrace                 | 273 ms                                                       | 253 ms: 1.08x faster                                                        |
| unpickle_pure_python     | 217 us                                                       | 202 us: 1.08x faster                                                        |
| json                     | 5.69 ms                                                      | 5.32 ms: 1.07x faster                                                       |
| chaos                    | 60.2 ms                                                      | 56.9 ms: 1.06x faster                                                       |
| django_template          | 36.4 ms                                                      | 34.4 ms: 1.06x faster                                                       |
| pathlib                  | 17.5 ms                                                      | 16.6 ms: 1.05x faster                                                       |
| 2to3                     | 293 ms                                                       | 279 ms: 1.05x faster                                                        |
| sympy_expand             | 509 ms                                                       | 485 ms: 1.05x faster                                                        |
| sympy_str                | 298 ms                                                       | 285 ms: 1.05x faster                                                        |
| regex_effbot             | 3.67 ms                                                      | 3.52 ms: 1.04x faster                                                       |
| sqlite_synth             | 2.91 us                                                      | 2.80 us: 1.04x faster                                                       |
| sympy_sum                | 155 ms                                                       | 149 ms: 1.04x faster                                                        |
| coroutines               | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                       |
| pickle_pure_python       | 323 us                                                       | 313 us: 1.03x faster                                                        |
| typing_runtime_protocols | 169 us                                                       | 164 us: 1.03x faster                                                        |
| comprehensions           | 17.0 us                                                      | 16.5 us: 1.03x faster                                                       |
| coverage                 | 80.0 ms                                                      | 77.6 ms: 1.03x faster                                                       |
| regex_dna                | 247 ms                                                       | 242 ms: 1.02x faster                                                        |
| async_generators         | 457 ms                                                       | 447 ms: 1.02x faster                                                        |
| nqueens                  | 90.7 ms                                                      | 89.4 ms: 1.01x faster                                                       |
| python_startup_no_site   | 8.96 ms                                                      | 8.90 ms: 1.01x faster                                                       |
| logging_simple           | 6.39 us                                                      | 6.45 us: 1.01x slower                                                       |
| pycparser                | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                      |
| docutils                 | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                      |
| logging_format           | 6.94 us                                                      | 7.19 us: 1.04x slower                                                       |
| crypto_pyaes             | 73.3 ms                                                      | 76.3 ms: 1.04x slower                                                       |
| fannkuch                 | 363 ms                                                       | 379 ms: 1.04x slower                                                        |
| meteor_contest           | 130 ms                                                       | 135 ms: 1.04x slower                                                        |
| nbody                    | 89.3 ms                                                      | 94.6 ms: 1.06x slower                                                       |
| mako                     | 10.4 ms                                                      | 11.1 ms: 1.07x slower                                                       |
| json_loads               | 24.7 us                                                      | 26.3 us: 1.07x slower                                                       |
| json_dumps               | 11.1 ms                                                      | 12.0 ms: 1.08x slower                                                       |
| many_optionals           | 930 us                                                       | 1.00 ms: 1.08x slower                                                       |
| create_gc_cycles         | 2.68 ms                                                      | 2.90 ms: 1.08x slower                                                       |
| regex_v8                 | 26.1 ms                                                      | 28.3 ms: 1.08x slower                                                       |
| xml_etree_parse          | 150 ms                                                       | 167 ms: 1.11x slower                                                        |
| gc_traversal             | 4.74 ms                                                      | 5.42 ms: 1.14x slower                                                       |
| pidigits                 | 252 ms                                                       | 292 ms: 1.16x slower                                                        |
| subparsers               | 17.5 ms                                                      | 24.1 ms: 1.38x slower                                                       |
| logging_silent           | 97.9 ns                                                      | 504 ns: 5.15x slower                                                        |
| bench_mp_pool            | 5.12 ms                                                      | 1.22 sec: 238.90x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (4): asyncio_websockets, djangocms, bench_thread_pool, xml_etree_iterparse
Ignored benchmarks (18) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, connected_components, gevent_hub, gunicorn, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x