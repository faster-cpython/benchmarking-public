# Results vs. 3.13.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-x86_64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.7 ms: 1.10x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 328 ms: 1.42x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 626 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 623 ms: 1.33x faster                                                        |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 64.7 ms: 1.26x faster                                                       |
| pidigits       | 252 ms                                                       | 257 ms: 1.02x slower                                                        |
| nbody          | 89.3 ms                                                      | 99.6 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                       |
| regex_dna      | 247 ms                                                       | 223 ms: 1.11x faster                                                        |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.55 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.94 sec: 1.27x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 133 ms: 1.13x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 194 us: 1.12x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 80.2 ms: 1.08x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 56.8 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 95.8 ms: 1.07x faster                                                       |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.02x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 340 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.82 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 54.4 ms: 1.05x faster                                                       |
| django_template | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                       |
| mako            | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.30 sec: 1.96x faster                                                      |
| richards                   | 52.9 ms                                                      | 35.1 ms: 1.51x faster                                                       |
| deepcopy                   | 392 us                                                       | 275 us: 1.43x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 328 ms: 1.42x faster                                                        |
| richards_super             | 59.6 ms                                                      | 42.1 ms: 1.42x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 28.0 us: 1.38x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 626 ms: 1.35x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 623 ms: 1.33x faster                                                        |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.94 sec: 1.27x faster                                                      |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                                        |
| float                      | 81.3 ms                                                      | 64.7 ms: 1.26x faster                                                       |
| pyflate                    | 503 ms                                                       | 407 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 503 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 81.1 ms: 1.20x faster                                                       |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.19x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 2.89 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 506 ms: 1.15x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 59.4 ms: 1.15x faster                                                       |
| generators                 | 33.6 ms                                                      | 29.6 ms: 1.14x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                       |
| telco                      | 8.79 ms                                                      | 7.79 ms: 1.13x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 133 ms: 1.13x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 194 us: 1.12x faster                                                        |
| regex_dna                  | 247 ms                                                       | 223 ms: 1.11x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.55 sec: 1.11x faster                                                      |
| bpe_tokeniser              | 5.09 sec                                                     | 4.60 sec: 1.11x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 764 ms: 1.10x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 66.7 ms: 1.10x faster                                                       |
| thrift                     | 901 us                                                       | 832 us: 1.08x faster                                                        |
| scimark_fft                | 328 ms                                                       | 303 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 80.2 ms: 1.08x faster                                                       |
| json                       | 5.69 ms                                                      | 5.27 ms: 1.08x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                      |
| xml_etree_process          | 61.2 ms                                                      | 56.8 ms: 1.08x faster                                                       |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.8 ms: 1.07x faster                                                       |
| logging_simple             | 6.39 us                                                      | 5.96 us: 1.07x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.12 ms: 1.07x faster                                                       |
| pylint                     | 347 ms                                                       | 324 ms: 1.07x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.52 us: 1.06x faster                                                       |
| meteor_contest             | 130 ms                                                       | 122 ms: 1.06x faster                                                        |
| connected_components       | 432 ms                                                       | 407 ms: 1.06x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 93.2 ns: 1.05x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.0 ms: 1.05x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 54.4 ms: 1.05x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 17.0 ms: 1.03x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.55 ms: 1.03x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| async_generators           | 457 ms                                                       | 443 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                       |
| 2to3                       | 293 ms                                                       | 286 ms: 1.02x faster                                                        |
| sympy_str                  | 298 ms                                                       | 292 ms: 1.02x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                        |
| sympy_expand               | 509 ms                                                       | 500 ms: 1.02x faster                                                        |
| coverage                   | 80.0 ms                                                      | 78.5 ms: 1.02x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 96.9 ms: 1.02x faster                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 8.82 ms: 1.02x faster                                                       |
| mako                       | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.02x slower                                                       |
| pidigits                   | 252 ms                                                       | 257 ms: 1.02x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 92.7 ms: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                       |
| fannkuch                   | 363 ms                                                       | 372 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                       |
| raytrace                   | 273 ms                                                       | 284 ms: 1.04x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.01 ms: 1.05x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.82 ms: 1.05x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 340 us: 1.05x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 78.1 ms: 1.07x slower                                                       |
| nbody                      | 89.3 ms                                                      | 99.6 ms: 1.12x slower                                                       |
| many_optionals             | 930 us                                                       | 1.06 ms: 1.14x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.42 ms: 1.35x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 25.0 ms: 1.43x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                                |

Benchmark hidden because not significant (5): typing_runtime_protocols, djangocms, chaos, pycparser, asyncio_websockets
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf2-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x