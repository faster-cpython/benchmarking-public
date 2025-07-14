# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 285 ms: 1.03x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 67.6 ms: 1.09x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                        |
| async_tree_none            | 376 ms                                                       | 276 ms: 1.36x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 334 ms: 1.36x faster                                                        |
| async_tree_io              | 843 ms                                                       | 628 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 629 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.5 ms: 1.28x faster                                                       |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 98.2 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 225 ms: 1.09x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.1 ms: 1.09x faster                                                       |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.57 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 196 us: 1.11x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 55.5 ms: 1.10x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 80.1 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.7 ms: 1.05x faster                                                       |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.5 us: 1.03x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.86 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.7 ms: 1.15x faster                                                       |
| mako            | 10.4 ms                                                      | 9.73 ms: 1.07x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                       |
| django_template | 36.4 ms                                                      | 35.4 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.28 sec: 1.99x faster                                                      |
| richards                   | 52.9 ms                                                      | 35.2 ms: 1.50x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 25.9 us: 1.49x faster                                                       |
| richards_super             | 59.6 ms                                                      | 40.5 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 334 ms: 1.40x faster                                                        |
| deepcopy                   | 392 us                                                       | 282 us: 1.39x faster                                                        |
| async_tree_none            | 376 ms                                                       | 276 ms: 1.36x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 334 ms: 1.36x faster                                                        |
| async_tree_io              | 843 ms                                                       | 628 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 629 ms: 1.32x faster                                                        |
| go                         | 162 ms                                                       | 126 ms: 1.29x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                      |
| float                      | 81.3 ms                                                      | 63.5 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 78.3 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| pyflate                    | 503 ms                                                       | 419 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                       |
| scimark_sor                | 123 ms                                                       | 104 ms: 1.19x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 2.88 ms: 1.19x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 58.8 ms: 1.16x faster                                                       |
| generators                 | 33.6 ms                                                      | 29.1 ms: 1.15x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 22.7 ms: 1.15x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.50 sec: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 744 ms: 1.13x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 196 us: 1.11x faster                                                        |
| scimark_fft                | 328 ms                                                       | 297 ms: 1.10x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 55.5 ms: 1.10x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.64 sec: 1.10x faster                                                      |
| regex_dna                  | 247 ms                                                       | 225 ms: 1.09x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.6 ms: 1.09x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 24.1 ms: 1.09x faster                                                       |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                        |
| thrift                     | 901 us                                                       | 831 us: 1.08x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 80.1 ms: 1.08x faster                                                       |
| pylint                     | 347 ms                                                       | 323 ms: 1.07x faster                                                        |
| json                       | 5.69 ms                                                      | 5.30 ms: 1.07x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| mako                       | 10.4 ms                                                      | 9.73 ms: 1.07x faster                                                       |
| meteor_contest             | 130 ms                                                       | 122 ms: 1.06x faster                                                        |
| connected_components       | 432 ms                                                       | 407 ms: 1.06x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.19 ms: 1.06x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.2 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.7 ms: 1.05x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 93.2 ns: 1.05x faster                                                       |
| logging_simple             | 6.39 us                                                      | 6.14 us: 1.04x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.69 us: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.03x faster                                                       |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                        |
| sympy_expand               | 509 ms                                                       | 494 ms: 1.03x faster                                                        |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| scimark_lu                 | 98.7 ms                                                      | 95.8 ms: 1.03x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.57 ms: 1.03x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.4 ms: 1.03x faster                                                       |
| 2to3                       | 293 ms                                                       | 285 ms: 1.03x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.5 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.86 ms: 1.01x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.25 sec: 1.01x slower                                                      |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                       |
| coverage                   | 80.0 ms                                                      | 81.2 ms: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.87 ms: 1.02x slower                                                       |
| fannkuch                   | 363 ms                                                       | 372 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| nqueens                    | 90.7 ms                                                      | 93.6 ms: 1.03x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.5 us: 1.03x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.5 ms: 1.04x slower                                                       |
| bench_thread_pool          | 942 us                                                       | 993 us: 1.05x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 77.7 ms: 1.06x slower                                                       |
| raytrace                   | 273 ms                                                       | 293 ms: 1.07x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.92 ms: 1.09x slower                                                       |
| nbody                      | 89.3 ms                                                      | 98.2 ms: 1.10x slower                                                       |
| many_optionals             | 930 us                                                       | 1.05 ms: 1.13x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 24.9 ms: 1.42x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.75 ms: 1.42x slower                                                       |
| telco                      | 8.79 ms                                                      | 160 ms: 18.26x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.27 sec: 248.73x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (3): djangocms, typing_runtime_protocols, chaos
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x