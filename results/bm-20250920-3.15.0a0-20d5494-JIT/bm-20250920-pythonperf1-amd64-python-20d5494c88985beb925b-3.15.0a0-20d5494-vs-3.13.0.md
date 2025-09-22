# Results vs. 3.13.0

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.082x faster
- HPT reliability: 87.52%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| sphinx         | 617 ms                                                      | 644 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 386 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 40.2 ms: 1.26x faster                                                      |
| nbody          | 66.3 ms                                                     | 54.6 ms: 1.21x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.8 ms: 1.61x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 106 us: 1.22x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.44 ms: 1.14x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.0 ms: 1.07x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.4 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.7 ms: 1.02x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.5 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.36 ms: 1.23x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 36.6 ms: 1.08x slower                                                      |
| django_template | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 522 us: 16.22x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.4 ms: 2.56x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.86x faster                                                       |
| mdp                        | 1.43 sec                                                    | 807 ms: 1.77x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.8 ms: 1.61x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 16.8 us: 1.37x faster                                                      |
| deepcopy                   | 223 us                                                      | 165 us: 1.36x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 386 ms: 1.29x faster                                                       |
| float                      | 50.8 ms                                                     | 40.2 ms: 1.26x faster                                                      |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                     |
| mako                       | 6.56 ms                                                     | 5.36 ms: 1.23x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.22x faster                                                       |
| nbody                      | 66.3 ms                                                     | 54.6 ms: 1.21x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.08 ms: 1.19x faster                                                      |
| fannkuch                   | 252 ms                                                      | 216 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.27 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.78 us: 1.14x faster                                                      |
| scimark_fft                | 175 ms                                                      | 154 ms: 1.14x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.44 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 338 ms: 1.13x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 864 ms: 1.13x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.54 sec: 1.13x faster                                                     |
| pyflate                    | 283 ms                                                      | 251 ms: 1.13x faster                                                       |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                                      |
| go                         | 84.7 ms                                                     | 76.5 ms: 1.11x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 439 ms: 1.11x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 50.0 ms: 1.07x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.60 sec: 1.06x faster                                                     |
| xml_etree_parse            | 92.2 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.4 ms: 1.03x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 62.4 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.1 ms: 1.02x faster                                                      |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.7 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.7 ms: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| sympy_expand               | 286 ms                                                      | 293 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.1 ms: 1.03x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 78.2 ms: 1.03x slower                                                      |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 74.2 ms: 1.03x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 88.1 ms: 1.03x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.04x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.28 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 644 ms: 1.04x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.5 ms: 1.05x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.06 us: 1.05x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.4 ms: 1.05x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.54 us: 1.06x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.08 ms: 1.06x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.5 ms: 1.07x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 873 us: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 36.6 ms: 1.08x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 91.4 ms: 1.08x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.13 ms: 1.09x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.3 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.3 ms: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.6 ms: 1.21x slower                                                      |
| many_optionals             | 361 us                                                      | 597 us: 1.65x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.8 ms: 2.93x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (7): pylint, crypto_pyaes, html5lib, shortest_path, logging_silent, typing_runtime_protocols, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 87.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown