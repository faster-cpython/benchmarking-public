# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-amd64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.029x faster
- HPT reliability: 56.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.73 sec: 1.13x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                       |
| sphinx         | 617 ms                                                      | 688 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                        |
| async_tree_io              | 513 ms                                                      | 406 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 353 ms: 1.08x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 54.3 ms: 1.22x faster                                                       |
| float          | 50.8 ms                                                     | 47.3 ms: 1.08x faster                                                       |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 18.4 ms: 1.30x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 80.0 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 110 us: 1.18x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 87.3 ms: 1.06x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 58.8 ms: 1.03x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.11 ms: 1.28x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 18.3 ms: 1.20x slower                                                       |
| django_template | 20.3 ms                                                     | 26.8 ms: 1.32x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 47.5 ms: 1.40x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 544 us: 15.57x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.9 us: 1.37x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 214 ms: 1.31x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 48.6 ms: 1.31x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 18.4 ms: 1.30x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.11 ms: 1.28x faster                                                       |
| async_tree_io              | 513 ms                                                      | 406 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 61.5 ms: 1.24x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.12 ms: 1.23x faster                                                       |
| nbody                      | 66.3 ms                                                     | 54.3 ms: 1.22x faster                                                       |
| async_tree_none            | 219 ms                                                      | 183 ms: 1.20x faster                                                        |
| scimark_fft                | 175 ms                                                      | 147 ms: 1.19x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 110 us: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 224 ms: 1.18x faster                                                        |
| deepcopy                   | 223 us                                                      | 190 us: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                      |
| json                       | 3.30 ms                                                     | 2.91 ms: 1.13x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.30 ms: 1.13x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 41.1 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 36.7 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.62 sec: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 353 ms: 1.08x faster                                                        |
| float                      | 50.8 ms                                                     | 47.3 ms: 1.08x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.3 ms: 1.06x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                       |
| shortest_path              | 355 ms                                                      | 341 ms: 1.04x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 54.5 ms: 1.04x faster                                                       |
| fannkuch                   | 252 ms                                                      | 243 ms: 1.04x faster                                                        |
| connected_components       | 320 ms                                                      | 309 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.8 ms: 1.03x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 82.6 ms: 1.02x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 35.9 ms: 1.02x faster                                                       |
| pyflate                    | 283 ms                                                      | 279 ms: 1.01x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 80.0 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.00x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 985 ms: 1.01x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 40.5 ms: 1.01x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 76.0 ms: 1.01x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.29 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 495 ms: 1.02x slower                                                        |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                       |
| coverage                   | 45.3 ms                                                     | 46.6 ms: 1.03x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 74.3 ms: 1.03x slower                                                       |
| go                         | 84.7 ms                                                     | 88.8 ms: 1.05x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 40.1 ms: 1.05x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.5 ns: 1.05x slower                                                       |
| pycparser                  | 695 ms                                                      | 735 ms: 1.06x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.52 sec: 1.06x slower                                                      |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 91.7 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.26 us: 1.08x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.71 us: 1.09x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.09x slower                                                        |
| chaos                      | 37.9 ms                                                     | 41.4 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 844 us: 1.10x slower                                                        |
| sphinx                     | 617 ms                                                      | 688 ms: 1.11x slower                                                        |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 63.3 ms: 1.13x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.73 sec: 1.13x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.14x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.09 ms: 1.14x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 37.8 ms: 1.16x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 205 ms: 1.19x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 18.3 ms: 1.20x slower                                                       |
| richards_super             | 29.8 ms                                                     | 37.7 ms: 1.27x slower                                                       |
| generators                 | 19.0 ms                                                     | 24.2 ms: 1.27x slower                                                       |
| richards                   | 26.3 ms                                                     | 33.6 ms: 1.28x slower                                                       |
| many_optionals             | 361 us                                                      | 467 us: 1.29x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 5.01 ms: 1.30x slower                                                       |
| django_template            | 20.3 ms                                                     | 26.8 ms: 1.32x slower                                                       |
| raytrace                   | 153 ms                                                      | 213 ms: 1.39x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 47.5 ms: 1.40x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.49x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (6): create_gc_cycles, regex_dna, bench_thread_pool, gc_traversal, asyncio_websockets, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: mypy2

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 56.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown