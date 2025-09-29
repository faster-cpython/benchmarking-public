# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.075x faster
- HPT reliability: 96.30%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.58 sec: 1.03x slower                                                     |
| html5lib       | 38.2 ms                                                     | 37.1 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 206 ms: 1.37x faster                                                       |
| async_tree_io              | 513 ms                                                      | 380 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 383 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 63.0 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 77.9 ms: 1.04x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.36 ms: 1.15x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.0 ms: 1.02x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 136 us: 1.04x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 55.9 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.9 ms: 1.02x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.41 ms: 1.02x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 497 us: 17.02x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.0 ms: 2.59x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                       |
| mdp                        | 1.43 sec                                                    | 796 ms: 1.80x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 16.4 us: 1.41x faster                                                      |
| deepcopy                   | 223 us                                                      | 163 us: 1.37x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 206 ms: 1.37x faster                                                       |
| async_tree_io              | 513 ms                                                      | 380 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 383 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.13 ms: 1.18x faster                                                      |
| float                      | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.36 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.77 us: 1.14x faster                                                      |
| json                       | 3.30 ms                                                     | 2.89 ms: 1.14x faster                                                      |
| go                         | 84.7 ms                                                     | 75.2 ms: 1.13x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| pylint                     | 205 ms                                                      | 191 ms: 1.08x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                      |
| nbody                      | 66.3 ms                                                     | 63.0 ms: 1.05x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 72.9 ms: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.50 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 77.9 ms: 1.04x faster                                                      |
| pyflate                    | 283 ms                                                      | 274 ms: 1.03x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 38.8 ms: 1.03x faster                                                      |
| html5lib                   | 38.2 ms                                                     | 37.1 ms: 1.03x faster                                                      |
| scimark_fft                | 175 ms                                                      | 170 ms: 1.03x faster                                                       |
| mako                       | 6.56 ms                                                     | 6.41 ms: 1.02x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.02x faster                                                     |
| spectral_norm              | 63.4 ms                                                     | 62.2 ms: 1.02x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 476 ms: 1.02x faster                                                       |
| sympy_expand               | 286 ms                                                      | 282 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.01x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                      |
| sympy_str                  | 167 ms                                                      | 165 ms: 1.01x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 972 ms: 1.00x faster                                                       |
| richards_super             | 29.8 ms                                                     | 30.0 ms: 1.01x slower                                                      |
| richards                   | 26.3 ms                                                     | 26.5 ms: 1.01x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 72.6 ms: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.84 us: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| python_startup             | 24.4 ms                                                     | 24.9 ms: 1.02x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 829 us: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.0 ms: 1.02x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.33 us: 1.02x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.26 ms: 1.03x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.95 sec: 1.03x slower                                                     |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| fannkuch                   | 252 ms                                                      | 259 ms: 1.03x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.58 sec: 1.03x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 56.5 ns: 1.04x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.2 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.99 ms: 1.04x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 136 us: 1.04x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 55.9 ms: 1.05x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 89.4 ms: 1.06x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.07x slower                                                      |
| coverage                   | 45.3 ms                                                     | 48.9 ms: 1.08x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.9 ms: 1.08x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 62.0 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.13 ms: 1.13x slower                                                      |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 560 us: 1.55x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 30.2 ms: 2.78x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (9): pidigits, sphinx, tomli_loads, pycparser, sympy_sum, shortest_path, 2to3, genshi_xml, scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 96.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown