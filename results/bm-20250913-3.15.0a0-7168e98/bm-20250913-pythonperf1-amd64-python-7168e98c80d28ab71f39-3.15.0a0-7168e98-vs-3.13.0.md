# Results vs. 3.13.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.070x faster
- HPT reliability: 75.09%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| html5lib       | 38.2 ms                                                     | 37.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 166 ms: 1.81x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 390 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 382 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.5 ms: 1.20x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 77.3 ms: 1.04x faster                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.44 ms: 1.14x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 86.3 ms: 1.07x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.1 ms: 1.03x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.9 ms: 1.02x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.5 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                      |
| mako            | 6.56 ms                                                     | 6.67 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 502 us: 16.86x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.8 ms: 2.62x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 166 ms: 1.81x faster                                                       |
| mdp                        | 1.43 sec                                                    | 800 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 16.6 us: 1.39x faster                                                      |
| deepcopy                   | 223 us                                                      | 166 us: 1.35x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 390 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 382 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 176 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                       |
| float                      | 50.8 ms                                                     | 42.5 ms: 1.20x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.14 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                       |
| json                       | 3.30 ms                                                     | 2.89 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.77 us: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 336 ms: 1.14x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.44 ms: 1.14x faster                                                      |
| go                         | 84.7 ms                                                     | 75.5 ms: 1.12x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                      |
| pylint                     | 205 ms                                                      | 191 ms: 1.08x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 86.3 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 77.3 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.51 ms: 1.04x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.5 ms: 1.02x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 39.3 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                     |
| html5lib                   | 38.2 ms                                                     | 37.5 ms: 1.02x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 62.5 ms: 1.01x faster                                                      |
| sympy_str                  | 167 ms                                                      | 165 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.5 ms: 1.01x faster                                                      |
| generators                 | 19.0 ms                                                     | 18.9 ms: 1.01x faster                                                      |
| genshi_text                | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 72.6 ms: 1.01x slower                                                      |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.2 ns: 1.01x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.67 ms: 1.02x slower                                                      |
| python_startup             | 24.4 ms                                                     | 24.9 ms: 1.02x slower                                                      |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                      |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.5 ms: 1.03x slower                                                      |
| scimark_fft                | 175 ms                                                      | 180 ms: 1.03x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.3 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                     |
| xml_etree_generate         | 53.5 ms                                                     | 55.1 ms: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 836 us: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.98 us: 1.04x slower                                                      |
| fannkuch                   | 252 ms                                                      | 261 ms: 1.04x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 87.8 ms: 1.04x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.46 us: 1.05x slower                                                      |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.04 ms: 1.05x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| coverage                   | 45.3 ms                                                     | 48.8 ms: 1.08x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.9 ms: 1.08x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.13 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.5 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.5 ms: 1.10x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 177 ms: 1.16x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.20 ms: 1.16x slower                                                      |
| django_template            | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                      |
| many_optionals             | 361 us                                                      | 551 us: 1.52x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.9 ms: 2.76x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (13): k_core, nbody, pprint_safe_repr, sympy_expand, sympy_integrate, pyflate, 2to3, pprint_pformat, shortest_path, xml_etree_iterparse, sphinx, genshi_xml, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 75.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown