# Results vs. 3.13.0

- fork: python
- ref: dbd23790dbd662169905
- machine: windows-amd64
- commit hash: dbd2379
- commit date: 2024-11-23
- overall geometric mean: 1.021x faster
- HPT reliability: 93.78%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 225 ms: 1.02x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.79 sec: 1.14x slower                                                      |
| sphinx         | 633 ms                                                      | 695 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                        |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 308 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 401 ms: 1.05x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 411 ms: 1.09x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 579 ms: 1.12x slower                                                        |
| async_tree_io              | 521 ms                                                      | 588 ms: 1.13x slower                                                        |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 52.4 ms: 1.30x faster                                                       |
| float          | 49.9 ms                                                     | 47.2 ms: 1.06x faster                                                       |
| pidigits       | 148 ms                                                      | 147 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.1 ms: 1.41x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.49 ms: 1.06x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 85.1 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 108 us: 1.24x faster                                                        |
| tomli_loads          | 1.39 sec                                                    | 1.26 sec: 1.11x faster                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 50.7 ms: 1.07x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 35.8 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.5 ms: 1.03x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.27 ms: 1.06x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 211 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.2 ms: 1.10x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.1 ms: 1.06x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.15 ms: 1.23x faster                                                       |
| django_template | 22.4 ms                                                     | 26.1 ms: 1.17x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 18.4 ms: 1.18x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 44.3 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 530 us: 16.60x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 15.8 us: 1.48x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.1 ms: 1.41x faster                                                       |
| nbody                      | 68.4 ms                                                     | 52.4 ms: 1.30x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 108 us: 1.24x faster                                                        |
| mako                       | 6.35 ms                                                     | 5.15 ms: 1.23x faster                                                       |
| deepcopy                   | 226 us                                                      | 188 us: 1.20x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 64.1 ms: 1.19x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 53.3 ms: 1.18x faster                                                       |
| scimark_fft                | 172 ms                                                      | 153 ms: 1.13x faster                                                        |
| crypto_pyaes               | 45.4 ms                                                     | 40.4 ms: 1.12x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.4 ms: 1.12x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.33 ms: 1.11x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.26 sec: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.24 ms: 1.10x faster                                                       |
| python_startup             | 25.4 ms                                                     | 23.2 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.88 us: 1.09x faster                                                       |
| async_tree_none            | 226 ms                                                      | 209 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 2.91 sec                                                    | 2.69 sec: 1.08x faster                                                      |
| json                       | 3.19 ms                                                     | 2.97 ms: 1.07x faster                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 50.7 ms: 1.07x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.85 ms: 1.07x faster                                                       |
| connected_components       | 332 ms                                                      | 313 ms: 1.06x faster                                                        |
| pathlib                    | 80.9 ms                                                     | 76.5 ms: 1.06x faster                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.1 ms: 1.06x faster                                                       |
| float                      | 49.9 ms                                                     | 47.2 ms: 1.06x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.49 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 82.2 ms: 1.05x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 806 us: 1.05x faster                                                        |
| pprint_safe_repr           | 494 ms                                                      | 473 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.0 ms                                                     | 35.8 ms: 1.03x faster                                                       |
| asyncio_websockets         | 318 ms                                                      | 308 ms: 1.03x faster                                                        |
| pprint_pformat             | 999 ms                                                      | 970 ms: 1.03x faster                                                        |
| shortest_path              | 362 ms                                                      | 352 ms: 1.03x faster                                                        |
| meteor_contest             | 73.5 ms                                                     | 72.4 ms: 1.02x faster                                                       |
| pidigits                   | 148 ms                                                      | 147 ms: 1.00x faster                                                        |
| pyflate                    | 283 ms                                                      | 284 ms: 1.00x slower                                                        |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| fannkuch                   | 253 ms                                                      | 258 ms: 1.02x slower                                                        |
| 2to3                       | 221 ms                                                      | 225 ms: 1.02x slower                                                        |
| logging_simple             | 5.96 us                                                     | 6.10 us: 1.02x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.5 ms: 1.03x slower                                                       |
| pycparser                  | 683 ms                                                      | 705 ms: 1.03x slower                                                        |
| coverage                   | 45.6 ms                                                     | 47.0 ms: 1.03x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 55.2 ms: 1.04x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.53 us: 1.04x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.31 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 401 ms: 1.05x slower                                                        |
| chaos                      | 38.5 ms                                                     | 40.5 ms: 1.05x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.5 ns: 1.05x slower                                                       |
| go                         | 87.0 ms                                                     | 91.7 ms: 1.05x slower                                                       |
| sympy_expand               | 291 ms                                                      | 307 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 112 us: 1.06x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 85.1 ms: 1.06x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.27 ms: 1.06x slower                                                       |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 93.7 ms: 1.08x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 411 ms: 1.09x slower                                                        |
| sphinx                     | 633 ms                                                      | 695 ms: 1.10x slower                                                        |
| pickle_pure_python         | 190 us                                                      | 211 us: 1.11x slower                                                        |
| sympy_integrate            | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 579 ms: 1.12x slower                                                        |
| nqueens                    | 56.7 ms                                                     | 63.4 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 588 ms: 1.13x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 878 us: 1.14x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.79 sec: 1.14x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 37.9 ms: 1.15x slower                                                       |
| k_core                     | 1.74 sec                                                    | 2.01 sec: 1.16x slower                                                      |
| django_template            | 22.4 ms                                                     | 26.1 ms: 1.17x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 205 ms: 1.17x slower                                                        |
| genshi_text                | 15.6 ms                                                     | 18.4 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.13 ms: 1.18x slower                                                       |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                        |
| richards_super             | 30.9 ms                                                     | 37.3 ms: 1.21x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                       |
| richards                   | 27.3 ms                                                     | 33.3 ms: 1.22x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 44.3 ms: 1.25x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.99 ms: 1.28x slower                                                       |
| raytrace                   | 160 ms                                                      | 209 ms: 1.31x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (6): pylint, async_tree_none_tg, dulwich_log, html5lib, xml_etree_parse, async_tree_memoization
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 93.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown