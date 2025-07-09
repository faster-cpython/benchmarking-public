# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_targets
- machine: linux-x86_64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.045x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                     |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                   |
| html5lib       | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                    |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                     |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                     |
| async_tree_none            | 376 ms                                                       | 276 ms: 1.36x faster                                                     |
| async_tree_io              | 843 ms                                                       | 626 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 831 ms                                                       | 631 ms: 1.32x faster                                                     |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                     |
| async_generators           | 457 ms                                                       | 445 ms: 1.03x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                    |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                     |
| nbody          | 89.3 ms                                                      | 101 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                        | 1.04x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                    |
| regex_dna      | 247 ms                                                       | 227 ms: 1.09x faster                                                     |
| regex_compile  | 143 ms                                                       | 133 ms: 1.08x faster                                                     |
| regex_effbot   | 3.67 ms                                                      | 3.65 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.93 sec: 1.27x faster                                                   |
| unpickle_pure_python | 217 us                                                       | 196 us: 1.11x faster                                                     |
| xml_etree_process    | 61.2 ms                                                      | 55.7 ms: 1.10x faster                                                    |
| xml_etree_generate   | 86.5 ms                                                      | 79.4 ms: 1.09x faster                                                    |
| xml_etree_parse      | 150 ms                                                       | 141 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 103 ms                                                       | 98.9 ms: 1.04x faster                                                    |
| pickle_pure_python   | 323 us                                                       | 331 us: 1.02x slower                                                     |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                             |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                    |
| python_startup_no_site | 8.96 ms                                                      | 8.87 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                    |
| genshi_xml      | 57.1 ms                                                      | 54.4 ms: 1.05x faster                                                    |
| mako            | 10.4 ms                                                      | 9.94 ms: 1.04x faster                                                    |
| django_template | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                    |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                   |
| richards                   | 52.9 ms                                                      | 34.4 ms: 1.54x faster                                                    |
| richards_super             | 59.6 ms                                                      | 40.8 ms: 1.46x faster                                                    |
| deepcopy                   | 392 us                                                       | 279 us: 1.40x faster                                                     |
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                     |
| deepcopy_memo              | 38.6 us                                                      | 27.9 us: 1.39x faster                                                    |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                     |
| async_tree_none            | 376 ms                                                       | 276 ms: 1.36x faster                                                     |
| async_tree_io              | 843 ms                                                       | 626 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 831 ms                                                       | 631 ms: 1.32x faster                                                     |
| float                      | 81.3 ms                                                      | 63.6 ms: 1.28x faster                                                    |
| tomli_loads                | 2.46 sec                                                     | 1.93 sec: 1.27x faster                                                   |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                     |
| go                         | 162 ms                                                       | 128 ms: 1.26x faster                                                     |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                     |
| deltablue                  | 3.42 ms                                                      | 2.89 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 3.54 us                                                      | 3.00 us: 1.18x faster                                                    |
| pyflate                    | 503 ms                                                       | 427 ms: 1.18x faster                                                     |
| spectral_norm              | 97.0 ms                                                      | 83.0 ms: 1.17x faster                                                    |
| dulwich_log                | 68.2 ms                                                      | 58.6 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                     |
| generators                 | 33.6 ms                                                      | 29.7 ms: 1.13x faster                                                    |
| genshi_text                | 26.2 ms                                                      | 23.3 ms: 1.13x faster                                                    |
| regex_v8                   | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                    |
| pprint_pformat             | 1.72 sec                                                     | 1.54 sec: 1.12x faster                                                   |
| unpickle_pure_python       | 217 us                                                       | 196 us: 1.11x faster                                                     |
| bpe_tokeniser              | 5.09 sec                                                     | 4.59 sec: 1.11x faster                                                   |
| html5lib                   | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                    |
| pprint_safe_repr           | 843 ms                                                       | 766 ms: 1.10x faster                                                     |
| xml_etree_process          | 61.2 ms                                                      | 55.7 ms: 1.10x faster                                                    |
| xml_etree_generate         | 86.5 ms                                                      | 79.4 ms: 1.09x faster                                                    |
| regex_dna                  | 247 ms                                                       | 227 ms: 1.09x faster                                                     |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                   |
| regex_compile              | 143 ms                                                       | 133 ms: 1.08x faster                                                     |
| thrift                     | 901 us                                                       | 837 us: 1.08x faster                                                     |
| connected_components       | 432 ms                                                       | 404 ms: 1.07x faster                                                     |
| pylint                     | 347 ms                                                       | 326 ms: 1.07x faster                                                     |
| xml_etree_parse            | 150 ms                                                       | 141 ms: 1.07x faster                                                     |
| hexiom                     | 6.55 ms                                                      | 6.17 ms: 1.06x faster                                                    |
| json                       | 5.69 ms                                                      | 5.37 ms: 1.06x faster                                                    |
| shortest_path              | 460 ms                                                       | 437 ms: 1.05x faster                                                     |
| meteor_contest             | 130 ms                                                       | 123 ms: 1.05x faster                                                     |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                    |
| genshi_xml                 | 57.1 ms                                                      | 54.4 ms: 1.05x faster                                                    |
| scimark_fft                | 328 ms                                                       | 313 ms: 1.05x faster                                                     |
| logging_silent             | 97.9 ns                                                      | 93.4 ns: 1.05x faster                                                    |
| mako                       | 10.4 ms                                                      | 9.94 ms: 1.04x faster                                                    |
| xml_etree_iterparse        | 103 ms                                                       | 98.9 ms: 1.04x faster                                                    |
| django_template            | 36.4 ms                                                      | 35.0 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.7 ms: 1.04x faster                                                    |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                    |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                   |
| async_generators           | 457 ms                                                       | 445 ms: 1.03x faster                                                     |
| coverage                   | 80.0 ms                                                      | 77.9 ms: 1.03x faster                                                    |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                    |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                     |
| scimark_lu                 | 98.7 ms                                                      | 96.2 ms: 1.03x faster                                                    |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.02x faster                                                     |
| logging_simple             | 6.39 us                                                      | 6.24 us: 1.02x faster                                                    |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                     |
| sqlite_synth               | 2.91 us                                                      | 2.86 us: 1.02x faster                                                    |
| sympy_expand               | 509 ms                                                       | 502 ms: 1.01x faster                                                     |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                   |
| python_startup_no_site     | 8.96 ms                                                      | 8.87 ms: 1.01x faster                                                    |
| logging_format             | 6.94 us                                                      | 6.89 us: 1.01x faster                                                    |
| regex_effbot               | 3.67 ms                                                      | 3.65 ms: 1.01x faster                                                    |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                     |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.02x slower                                                    |
| pickle_pure_python         | 323 us                                                       | 331 us: 1.02x slower                                                     |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.03x slower                                                    |
| nqueens                    | 90.7 ms                                                      | 93.2 ms: 1.03x slower                                                    |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                   |
| coroutines                 | 21.6 ms                                                      | 22.2 ms: 1.03x slower                                                    |
| crypto_pyaes               | 73.3 ms                                                      | 77.3 ms: 1.05x slower                                                    |
| fannkuch                   | 363 ms                                                       | 384 ms: 1.06x slower                                                     |
| raytrace                   | 273 ms                                                       | 289 ms: 1.06x slower                                                     |
| create_gc_cycles           | 2.68 ms                                                      | 2.90 ms: 1.08x slower                                                    |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.18 ms: 1.08x slower                                                    |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.13x slower                                                     |
| many_optionals             | 930 us                                                       | 1.06 ms: 1.14x slower                                                    |
| gc_traversal               | 4.74 ms                                                      | 6.49 ms: 1.37x slower                                                    |
| subparsers                 | 17.5 ms                                                      | 25.3 ms: 1.45x slower                                                    |
| telco                      | 8.79 ms                                                      | 161 ms: 18.30x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                             |

Benchmark hidden because not significant (5): djangocms, chaos, asyncio_websockets, typing_runtime_protocols, json_dumps
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x