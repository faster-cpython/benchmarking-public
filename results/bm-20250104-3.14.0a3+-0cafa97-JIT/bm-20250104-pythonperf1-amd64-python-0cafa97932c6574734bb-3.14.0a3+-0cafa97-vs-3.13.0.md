# Results vs. 3.13.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.031x faster
- HPT reliability: 66.15%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| sphinx         | 617 ms                                                      | 674 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                        |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 346 ms: 1.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 52.4 ms: 1.27x faster                                                       |
| float          | 50.8 ms                                                     | 40.3 ms: 1.26x faster                                                       |
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 79.7 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 108 us: 1.20x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 49.6 ms: 1.08x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 86.1 ms: 1.07x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.7 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.3 ms: 1.02x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.5 ms: 1.04x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.6 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.06 ms: 1.30x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 18.7 ms: 1.23x slower                                                       |
| django_template | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 48.0 ms: 1.42x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 530 us: 15.98x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.2 us: 1.42x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.06 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                        |
| nbody                      | 66.3 ms                                                     | 52.4 ms: 1.27x faster                                                       |
| float                      | 50.8 ms                                                     | 40.3 ms: 1.26x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 50.6 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.09 ms: 1.25x faster                                                       |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.22x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 62.8 ms: 1.21x faster                                                       |
| scimark_fft                | 175 ms                                                      | 145 ms: 1.21x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 108 us: 1.20x faster                                                        |
| deepcopy                   | 223 us                                                      | 190 us: 1.18x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.24 ms: 1.14x faster                                                       |
| json                       | 3.30 ms                                                     | 2.90 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 36.7 ms: 1.11x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 41.3 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 346 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.65 sec: 1.08x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 49.6 ms: 1.08x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 86.1 ms: 1.07x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 53.5 ms: 1.06x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.5 ms: 1.04x faster                                                       |
| connected_components       | 320 ms                                                      | 310 ms: 1.03x faster                                                        |
| shortest_path              | 355 ms                                                      | 345 ms: 1.03x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 35.7 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.3 ms: 1.02x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 82.7 ms: 1.02x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 79.7 ms: 1.01x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 39.8 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                        |
| pathlib                    | 75.3 ms                                                     | 76.3 ms: 1.01x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 306 ms: 1.02x slower                                                        |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 74.4 ms: 1.03x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.5 ns: 1.03x slower                                                       |
| pycparser                  | 695 ms                                                      | 720 ms: 1.04x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 17.6 ms: 1.04x slower                                                       |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| coverage                   | 45.3 ms                                                     | 47.1 ms: 1.04x slower                                                       |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                        |
| go                         | 84.7 ms                                                     | 89.9 ms: 1.06x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.53 sec: 1.07x slower                                                      |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.2 ms: 1.07x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.65 us: 1.08x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.25 us: 1.08x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.1 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.09x slower                                                        |
| sphinx                     | 617 ms                                                      | 674 ms: 1.09x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 838 us: 1.10x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 63.4 ms: 1.13x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.08 ms: 1.13x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.14x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 37.5 ms: 1.15x slower                                                       |
| async_generators           | 223 ms                                                      | 258 ms: 1.16x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 205 ms: 1.20x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.27 ms: 1.20x slower                                                       |
| generators                 | 19.0 ms                                                     | 23.2 ms: 1.22x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 18.7 ms: 1.23x slower                                                       |
| many_optionals             | 361 us                                                      | 457 us: 1.26x slower                                                        |
| richards_super             | 29.8 ms                                                     | 37.7 ms: 1.27x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.4 ms: 1.27x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 5.00 ms: 1.30x slower                                                       |
| raytrace                   | 153 ms                                                      | 202 ms: 1.32x slower                                                        |
| django_template            | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 48.0 ms: 1.42x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.8 ms: 1.46x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (12): regex_v8, json_loads, create_gc_cycles, pprint_pformat, pprint_safe_repr, fannkuch, pyflate, gc_traversal, json_dumps, html5lib, pylint, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: mypy2

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 66.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown