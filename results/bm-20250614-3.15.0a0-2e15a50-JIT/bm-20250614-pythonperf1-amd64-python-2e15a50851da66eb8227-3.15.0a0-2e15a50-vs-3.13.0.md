# Results vs. 3.13.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.276x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 288 ms: 1.34x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.11 sec: 1.38x slower                                                     |
| html5lib       | 38.2 ms                                                     | 51.9 ms: 1.36x slower                                                      |
| sphinx         | 617 ms                                                      | 849 ms: 1.38x slower                                                       |
| Geometric mean | (ref)                                                       | 1.36x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 284 ms: 1.01x slower                                                       |
| async_tree_io              | 513 ms                                                      | 531 ms: 1.04x slower                                                       |
| async_tree_none            | 219 ms                                                      | 232 ms: 1.06x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 285 ms: 1.08x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 551 ms: 1.11x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 430 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 432 ms: 1.14x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 228 ms: 1.14x slower                                                       |
| async_generators           | 223 ms                                                      | 355 ms: 1.59x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 25.7 ms: 2.06x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 56.2 ms: 1.18x faster                                                      |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| float          | 50.8 ms                                                     | 78.7 ms: 1.55x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.6 ms: 1.44x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.74 ms: 1.03x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 120 ms: 1.48x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| xml_etree_parse      | 92.2 ms                                                     | 105 ms: 1.14x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 157 us: 1.21x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 71.8 ms: 1.34x slower                                                      |
| json_loads           | 15.1 us                                                     | 20.9 us: 1.38x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 8.63 ms: 1.39x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 52.1 ms: 1.43x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 87.8 ms: 1.45x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 329 us: 1.77x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.35x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.2 ms: 1.12x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 7.25 ms: 1.10x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 50.7 ms: 1.50x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 24.7 ms: 1.62x slower                                                      |
| django_template | 20.3 ms                                                     | 38.0 ms: 1.87x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.50x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 34.8 ms: 2.16x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.88x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.6 ms: 1.44x faster                                                      |
| mdp                        | 1.43 sec                                                    | 1.19 sec: 1.20x faster                                                     |
| nbody                      | 66.3 ms                                                     | 56.2 ms: 1.18x faster                                                      |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 284 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.74 ms: 1.03x slower                                                      |
| async_tree_io              | 513 ms                                                      | 531 ms: 1.04x slower                                                       |
| async_tree_none            | 219 ms                                                      | 232 ms: 1.06x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.06 sec: 1.07x slower                                                     |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.80 ms: 1.07x slower                                                      |
| async_tree_memoization     | 265 ms                                                      | 285 ms: 1.08x slower                                                       |
| scimark_fft                | 175 ms                                                      | 189 ms: 1.08x slower                                                       |
| telco                      | 4.85 ms                                                     | 5.24 ms: 1.08x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.73 us: 1.09x slower                                                      |
| mako                       | 6.56 ms                                                     | 7.25 ms: 1.10x slower                                                      |
| async_tree_io_tg           | 497 ms                                                      | 551 ms: 1.11x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.2 ms: 1.12x slower                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 430 ms: 1.12x slower                                                       |
| fannkuch                   | 252 ms                                                      | 284 ms: 1.13x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 81.6 ms: 1.13x slower                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 432 ms: 1.14x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 228 ms: 1.14x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.56 sec: 1.14x slower                                                     |
| xml_etree_parse            | 92.2 ms                                                     | 105 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 157 us: 1.21x slower                                                       |
| json                       | 3.30 ms                                                     | 3.99 ms: 1.21x slower                                                      |
| deepcopy                   | 223 us                                                      | 271 us: 1.21x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.48 ms: 1.21x slower                                                      |
| pylint                     | 205 ms                                                      | 250 ms: 1.22x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 988 us: 1.22x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 105 ms: 1.25x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 52.2 ms: 1.30x slower                                                      |
| pycparser                  | 695 ms                                                      | 927 ms: 1.33x slower                                                       |
| 2to3                       | 215 ms                                                      | 288 ms: 1.34x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 71.8 ms: 1.34x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 115 ms: 1.35x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 51.9 ms: 1.36x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 62.0 ms: 1.36x slower                                                      |
| pyflate                    | 283 ms                                                      | 387 ms: 1.37x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.77 us: 1.37x slower                                                      |
| sphinx                     | 617 ms                                                      | 849 ms: 1.38x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.11 sec: 1.38x slower                                                     |
| sympy_integrate            | 12.3 ms                                                     | 17.0 ms: 1.38x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 670 ms: 1.38x slower                                                       |
| json_loads                 | 15.1 us                                                     | 20.9 us: 1.38x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 8.63 ms: 1.39x slower                                                      |
| sympy_str                  | 167 ms                                                      | 233 ms: 1.40x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.37 sec: 1.40x slower                                                     |
| typing_runtime_protocols   | 103 us                                                      | 144 us: 1.40x slower                                                       |
| sympy_expand               | 286 ms                                                      | 404 ms: 1.42x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 52.1 ms: 1.43x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 87.8 ms: 1.45x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.85 ms: 1.45x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 120 ms: 1.48x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 50.7 ms: 1.50x slower                                                      |
| deepcopy_memo              | 23.1 us                                                     | 35.1 us: 1.52x slower                                                      |
| comprehensions             | 10.4 us                                                     | 15.8 us: 1.52x slower                                                      |
| float                      | 50.8 ms                                                     | 78.7 ms: 1.55x slower                                                      |
| many_optionals             | 361 us                                                      | 566 us: 1.57x slower                                                       |
| async_generators           | 223 ms                                                      | 355 ms: 1.59x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 90.4 ms: 1.61x slower                                                      |
| go                         | 84.7 ms                                                     | 137 ms: 1.62x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 24.7 ms: 1.62x slower                                                      |
| logging_format             | 6.18 us                                                     | 10.1 us: 1.63x slower                                                      |
| logging_simple             | 5.77 us                                                     | 9.44 us: 1.64x slower                                                      |
| chaos                      | 37.9 ms                                                     | 66.0 ms: 1.74x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 135 ms: 1.77x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 329 us: 1.77x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 73.7 ms: 1.81x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 115 ms: 1.82x slower                                                       |
| django_template            | 20.3 ms                                                     | 38.0 ms: 1.87x slower                                                      |
| generators                 | 19.0 ms                                                     | 37.3 ms: 1.96x slower                                                      |
| richards_super             | 29.8 ms                                                     | 58.5 ms: 1.96x slower                                                      |
| richards                   | 26.3 ms                                                     | 51.7 ms: 1.97x slower                                                      |
| raytrace                   | 153 ms                                                      | 307 ms: 2.00x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 7.80 ms: 2.03x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 25.7 ms: 2.06x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 22.6 ms: 2.08x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 122 ms: 2.15x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 4.57 ms: 2.42x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 501 ns: 9.19x slower                                                       |
| coverage                   | 45.3 ms                                                     | 473 ms: 10.44x slower                                                      |
| thrift                     | 8.47 ms                                                     | 104 ms: 12.28x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.41x slower                                                               |

Benchmark hidden because not significant (1): k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.276x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.22x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: unknown