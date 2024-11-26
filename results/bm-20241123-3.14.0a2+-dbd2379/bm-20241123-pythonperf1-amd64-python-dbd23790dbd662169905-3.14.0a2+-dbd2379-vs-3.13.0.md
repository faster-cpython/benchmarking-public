# Results vs. 3.13.0

- fork: python
- ref: dbd23790dbd662169905
- machine: windows-amd64
- commit hash: dbd2379
- commit date: 2024-11-23
- overall geometric mean: 1.030x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 224 ms: 1.01x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                      |
| html5lib       | 38.9 ms                                                     | 40.7 ms: 1.05x slower                                                       |
| sphinx         | 633 ms                                                      | 673 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                        |
| async_tree_none            | 226 ms                                                      | 213 ms: 1.06x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 302 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 397 ms: 1.04x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.5 ms: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 412 ms: 1.09x slower                                                        |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                        |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 580 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 56.5 ms: 1.13x slower                                                       |
| nbody          | 68.4 ms                                                     | 80.0 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.44 ms: 1.09x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 90.1 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 94.7 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.6 ms: 1.08x slower                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 58.4 ms: 1.08x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 41.4 ms: 1.12x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.63 ms: 1.12x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 152 us: 1.14x slower                                                        |
| pickle_pure_python   | 190 us                                                      | 229 us: 1.21x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.6 ms: 1.08x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.2 ms: 1.05x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 36.9 ms: 1.04x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                       |
| mako            | 6.35 ms                                                     | 7.00 ms: 1.10x slower                                                       |
| django_template | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 535 us: 16.44x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                                       |
| deepcopy                   | 226 us                                                      | 189 us: 1.20x faster                                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                        |
| pylint                     | 211 ms                                                      | 189 ms: 1.11x faster                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.44 ms: 1.09x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 21.5 us: 1.08x faster                                                       |
| python_startup             | 25.4 ms                                                     | 23.6 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.92 us: 1.07x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 76.1 ms: 1.06x faster                                                       |
| async_tree_none            | 226 ms                                                      | 213 ms: 1.06x faster                                                        |
| bench_mp_pool              | 86.4 ms                                                     | 81.9 ms: 1.06x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.87 ms: 1.05x faster                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.2 ms: 1.05x faster                                                       |
| asyncio_websockets         | 318 ms                                                      | 302 ms: 1.05x faster                                                        |
| bench_thread_pool          | 847 us                                                      | 807 us: 1.05x faster                                                        |
| json                       | 3.19 ms                                                     | 3.04 ms: 1.05x faster                                                       |
| shortest_path              | 362 ms                                                      | 353 ms: 1.02x faster                                                        |
| connected_components       | 332 ms                                                      | 327 ms: 1.02x faster                                                        |
| telco                      | 4.79 ms                                                     | 4.75 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 94.7 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| 2to3                       | 221 ms                                                      | 224 ms: 1.01x slower                                                        |
| coverage                   | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 89.4 ms: 1.03x slower                                                       |
| go                         | 87.0 ms                                                     | 89.7 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 397 ms: 1.04x slower                                                        |
| genshi_xml                 | 35.5 ms                                                     | 36.9 ms: 1.04x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 42.5 ms: 1.04x slower                                                       |
| sympy_expand               | 291 ms                                                      | 304 ms: 1.04x slower                                                        |
| html5lib                   | 38.9 ms                                                     | 40.7 ms: 1.05x slower                                                       |
| bpe_tokeniser              | 2.91 sec                                                    | 3.05 sec: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 177 ms: 1.05x slower                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 1.33 ms: 1.06x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.5 ms: 1.06x slower                                                       |
| sphinx                     | 633 ms                                                      | 673 ms: 1.06x slower                                                        |
| meteor_contest             | 73.5 ms                                                     | 78.2 ms: 1.06x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.34 us: 1.06x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.48 sec: 1.07x slower                                                      |
| pycparser                  | 683 ms                                                      | 732 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 113 us: 1.07x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.69 sec: 1.07x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 48.8 ms: 1.07x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.6 ms: 1.08x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.76 us: 1.08x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 58.4 ms: 1.08x slower                                                       |
| spectral_norm              | 62.8 ms                                                     | 67.9 ms: 1.08x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 412 ms: 1.09x slower                                                        |
| genshi_text                | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                       |
| mako                       | 6.35 ms                                                     | 7.00 ms: 1.10x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.71 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 193 ms: 1.11x slower                                                        |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 32.9 ms                                                     | 36.5 ms: 1.11x slower                                                       |
| django_template            | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                       |
| xml_etree_process          | 37.0 ms                                                     | 41.4 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 582 ms: 1.12x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 580 ms: 1.12x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 90.1 ms: 1.12x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.63 ms: 1.12x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 555 ms: 1.12x slower                                                        |
| pprint_pformat             | 999 ms                                                      | 1.13 sec: 1.13x slower                                                      |
| float                      | 49.9 ms                                                     | 56.5 ms: 1.13x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 64.5 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 152 us: 1.14x slower                                                        |
| fannkuch                   | 253 ms                                                      | 289 ms: 1.14x slower                                                        |
| pyflate                    | 283 ms                                                      | 324 ms: 1.14x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.4 ms: 1.15x slower                                                       |
| chaos                      | 38.5 ms                                                     | 44.4 ms: 1.15x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.49 ms: 1.15x slower                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 47.5 ms: 1.16x slower                                                       |
| scimark_fft                | 172 ms                                                      | 201 ms: 1.17x slower                                                        |
| nbody                      | 68.4 ms                                                     | 80.0 ms: 1.17x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 64.0 ns: 1.17x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 89.7 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.19x slower                                                       |
| comprehensions             | 10.3 us                                                     | 12.2 us: 1.19x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 921 us: 1.19x slower                                                        |
| scimark_lu                 | 53.0 ms                                                     | 63.9 ms: 1.21x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 229 us: 1.21x slower                                                        |
| richards_super             | 30.9 ms                                                     | 37.4 ms: 1.21x slower                                                       |
| k_core                     | 1.74 sec                                                    | 2.11 sec: 1.22x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                       |
| richards                   | 27.3 ms                                                     | 33.4 ms: 1.22x slower                                                       |
| raytrace                   | 160 ms                                                      | 202 ms: 1.26x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (3): pidigits, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.030x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown