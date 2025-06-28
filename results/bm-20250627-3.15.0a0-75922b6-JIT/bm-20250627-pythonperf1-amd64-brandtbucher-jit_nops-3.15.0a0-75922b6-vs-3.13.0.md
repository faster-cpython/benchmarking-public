# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_nops
- machine: windows-amd64
- commit hash: 75922b6
- commit date: 2025-06-27
- overall geometric mean: 1.080x faster
- HPT reliability: 79.40%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                 |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                               |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                       | 1.04x slower                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                 |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                 |
| async_tree_io_tg           | 497 ms                                                      | 387 ms: 1.28x faster                                                 |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                 |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                 |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                 |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                 |
| coroutines                 | 12.5 ms                                                     | 15.2 ms: 1.22x slower                                                |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 54.3 ms: 1.22x faster                                                |
| float          | 50.8 ms                                                     | 45.5 ms: 1.12x faster                                                |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                       | 1.11x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                |
| regex_compile  | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                       | 1.18x faster                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 107 us: 1.21x faster                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                               |
| xml_etree_generate   | 53.5 ms                                                     | 50.4 ms: 1.06x faster                                                |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                |
| xml_etree_parse      | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                |
| xml_etree_process    | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.2 ms: 1.05x slower                                                |
| json_dumps           | 6.19 ms                                                     | 6.55 ms: 1.06x slower                                                |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.38 ms: 1.22x faster                                                |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 490 us: 17.26x faster                                                |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.36x faster                                                |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                 |
| mdp                        | 1.43 sec                                                    | 804 ms: 1.78x faster                                                 |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                 |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                 |
| async_tree_io_tg           | 497 ms                                                      | 387 ms: 1.28x faster                                                 |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                 |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                |
| nbody                      | 66.3 ms                                                     | 54.3 ms: 1.22x faster                                                |
| mako                       | 6.56 ms                                                     | 5.38 ms: 1.22x faster                                                |
| unpickle_pure_python       | 130 us                                                      | 107 us: 1.21x faster                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                               |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                 |
| scimark_fft                | 175 ms                                                      | 152 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.29 ms: 1.14x faster                                                |
| telco                      | 4.85 ms                                                     | 4.29 ms: 1.13x faster                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.57 sec: 1.12x faster                                               |
| float                      | 50.8 ms                                                     | 45.5 ms: 1.12x faster                                                |
| fannkuch                   | 252 ms                                                      | 227 ms: 1.11x faster                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.11x faster                                                |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                |
| pyflate                    | 283 ms                                                      | 258 ms: 1.10x faster                                                 |
| json                       | 3.30 ms                                                     | 3.05 ms: 1.08x faster                                                |
| go                         | 84.7 ms                                                     | 78.6 ms: 1.08x faster                                                |
| xml_etree_generate         | 53.5 ms                                                     | 50.4 ms: 1.06x faster                                                |
| pprint_safe_repr           | 485 ms                                                      | 459 ms: 1.06x faster                                                 |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                |
| pprint_pformat             | 977 ms                                                      | 936 ms: 1.04x faster                                                 |
| xml_etree_parse            | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                               |
| regex_compile              | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                |
| xml_etree_process          | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                 |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.01x faster                                                |
| logging_silent             | 54.6 ns                                                     | 55.0 ns: 1.01x slower                                                |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                 |
| meteor_contest             | 72.0 ms                                                     | 72.6 ms: 1.01x slower                                                |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                                 |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.5 ms: 1.02x slower                                                |
| crypto_pyaes               | 45.6 ms                                                     | 46.4 ms: 1.02x slower                                                |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.02x slower                                                |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                 |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.02x slower                                                |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.03x slower                                                 |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                 |
| sympy_sum                  | 85.2 ms                                                     | 87.9 ms: 1.03x slower                                                |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                |
| sympy_expand               | 286 ms                                                      | 295 ms: 1.03x slower                                                 |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                |
| spectral_norm              | 63.4 ms                                                     | 65.9 ms: 1.04x slower                                                |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.2 ms: 1.05x slower                                                |
| json_dumps                 | 6.19 ms                                                     | 6.55 ms: 1.06x slower                                                |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                |
| scimark_sor                | 76.2 ms                                                     | 81.1 ms: 1.06x slower                                                |
| nqueens                    | 56.1 ms                                                     | 60.0 ms: 1.07x slower                                                |
| scimark_lu                 | 56.7 ms                                                     | 60.9 ms: 1.07x slower                                                |
| logging_simple             | 5.77 us                                                     | 6.21 us: 1.08x slower                                                |
| logging_format             | 6.18 us                                                     | 6.66 us: 1.08x slower                                                |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                               |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.09x slower                                                |
| chaos                      | 37.9 ms                                                     | 41.6 ms: 1.10x slower                                                |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                |
| hexiom                     | 3.84 ms                                                     | 4.24 ms: 1.10x slower                                                |
| coverage                   | 45.3 ms                                                     | 50.6 ms: 1.12x slower                                                |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                 |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                 |
| deltablue                  | 1.89 ms                                                     | 2.23 ms: 1.18x slower                                                |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                |
| coroutines                 | 12.5 ms                                                     | 15.2 ms: 1.22x slower                                                |
| many_optionals             | 361 us                                                      | 446 us: 1.23x slower                                                 |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                                |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                         |

Benchmark hidden because not significant (5): pylint, regex_dna, pycparser, html5lib, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250627-3.15.0a0-75922b6-JIT/bm-20250627-pythonperf1-amd64-brandtbucher-jit_nops-3.15.0a0-75922b6.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 79.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown