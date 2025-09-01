# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.100x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.01x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| html5lib       | 38.2 ms                                                     | 37.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.35x faster                                                       |
| async_tree_io              | 513 ms                                                      | 386 ms: 1.33x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 200 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 380 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 332 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 242 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 52.3 ms: 1.27x faster                                                      |
| float          | 50.8 ms                                                     | 42.8 ms: 1.19x faster                                                      |
| pidigits       | 146 ms                                                      | 144 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.7 ms: 1.75x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.3 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.48 ms: 1.13x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 49.6 ms: 1.08x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.8 ms: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.1 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.0 ms: 1.02x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 203 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.25 ms: 1.25x faster                                                      |
| django_template | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 495 us: 17.11x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.7 ms: 2.54x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| mdp                        | 1.43 sec                                                    | 783 ms: 1.83x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.7 ms: 1.75x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.35x faster                                                       |
| async_tree_io              | 513 ms                                                      | 386 ms: 1.33x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 200 ms: 1.32x faster                                                       |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 380 ms: 1.31x faster                                                       |
| telco                      | 4.85 ms                                                     | 3.75 ms: 1.29x faster                                                      |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| nbody                      | 66.3 ms                                                     | 52.3 ms: 1.27x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                     |
| mako                       | 6.56 ms                                                     | 5.25 ms: 1.25x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.1 us: 1.21x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                       |
| scimark_fft                | 175 ms                                                      | 146 ms: 1.20x faster                                                       |
| fannkuch                   | 252 ms                                                      | 211 ms: 1.19x faster                                                       |
| float                      | 50.8 ms                                                     | 42.8 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.23 ms: 1.17x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.47 sec: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 332 ms: 1.15x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 849 ms: 1.15x faster                                                       |
| json                       | 3.30 ms                                                     | 2.88 ms: 1.15x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 424 ms: 1.14x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.48 ms: 1.13x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 77.4 ms: 1.09x faster                                                      |
| pyflate                    | 283 ms                                                      | 260 ms: 1.09x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 49.6 ms: 1.08x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                     |
| pylint                     | 205 ms                                                      | 193 ms: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.8 ms: 1.05x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.1 ms: 1.04x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 38.7 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.3 ms: 1.03x faster                                                      |
| shortest_path              | 355 ms                                                      | 348 ms: 1.02x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 62.1 ms: 1.02x faster                                                      |
| pidigits                   | 146 ms                                                      | 144 ms: 1.02x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 37.5 ms: 1.02x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 44.9 ms: 1.02x faster                                                      |
| connected_components       | 320 ms                                                      | 315 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 71.1 ms: 1.01x faster                                                      |
| logging_silent             | 54.6 ns                                                     | 54.1 ns: 1.01x faster                                                      |
| sympy_sum                  | 85.2 ms                                                     | 84.4 ms: 1.01x faster                                                      |
| comprehensions             | 10.4 us                                                     | 10.3 us: 1.01x faster                                                      |
| sympy_str                  | 167 ms                                                      | 166 ms: 1.01x faster                                                       |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                      |
| 2to3                       | 215 ms                                                      | 218 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 291 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.0 ms: 1.02x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 78.2 ms: 1.03x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 58.2 ms: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 838 us: 1.03x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.01 us: 1.04x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.28 ms: 1.04x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.46 us: 1.05x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.1 ms: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| chaos                      | 37.9 ms                                                     | 40.2 ms: 1.06x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.07x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 242 ms: 1.08x slower                                                       |
| coverage                   | 45.3 ms                                                     | 49.3 ms: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 203 us: 1.09x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 93.3 ms: 1.11x slower                                                      |
| raytrace                   | 153 ms                                                      | 172 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.21 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                      |
| many_optionals             | 361 us                                                      | 555 us: 1.54x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.6 ms: 2.73x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (5): pycparser, genshi_xml, typing_runtime_protocols, genshi_text, sphinx
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.100x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown