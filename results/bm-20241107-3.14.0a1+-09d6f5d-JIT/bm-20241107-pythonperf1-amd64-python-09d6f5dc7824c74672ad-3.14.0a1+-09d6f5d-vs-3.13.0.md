# Results vs. 3.13.0

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: windows-amd64
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.002x faster
- HPT reliability: 88.28%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 243 ms: 1.10x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.89 sec: 1.21x slower                                                      |
| sphinx         | 633 ms                                                      | 760 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                        |
| async_tree_none            | 226 ms                                                      | 204 ms: 1.11x faster                                                        |
| async_tree_memoization     | 276 ms                                                      | 253 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 209 ms                                                      | 204 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 395 ms: 1.03x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.4 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 396 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 574 ms: 1.11x slower                                                        |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 56.3 ms: 1.21x faster                                                       |
| float          | 49.9 ms                                                     | 47.1 ms: 1.06x faster                                                       |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.5 ms: 1.48x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 116 ms: 1.00x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 91.2 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 35.6 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 92.8 ms: 1.01x faster                                                       |
| json_dumps           | 5.92 ms                                                     | 6.12 ms: 1.03x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                                        |
| pickle_pure_python   | 190 us                                                      | 207 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.5 ms: 1.08x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.06 ms: 1.26x faster                                                       |
| django_template | 22.4 ms                                                     | 27.3 ms: 1.22x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 19.3 ms: 1.24x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 46.8 ms: 1.32x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 530 us: 16.60x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 14.5 ms: 1.48x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 16.7 us: 1.39x faster                                                       |
| mako                       | 6.35 ms                                                     | 5.06 ms: 1.26x faster                                                       |
| nbody                      | 68.4 ms                                                     | 56.3 ms: 1.21x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 63.3 ms: 1.20x faster                                                       |
| deepcopy                   | 226 us                                                      | 191 us: 1.18x faster                                                        |
| spectral_norm              | 62.8 ms                                                     | 54.1 ms: 1.16x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 250 ms: 1.15x faster                                                        |
| crypto_pyaes               | 45.4 ms                                                     | 40.3 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 204 ms: 1.11x faster                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 37.0 ms: 1.10x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.87 us: 1.10x faster                                                       |
| scimark_fft                | 172 ms                                                      | 157 ms: 1.10x faster                                                        |
| tomli_loads                | 1.39 sec                                                    | 1.28 sec: 1.09x faster                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.25 ms: 1.09x faster                                                       |
| json                       | 3.19 ms                                                     | 2.93 ms: 1.09x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 253 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 2.91 sec                                                    | 2.68 sec: 1.09x faster                                                      |
| pprint_safe_repr           | 494 ms                                                      | 455 ms: 1.08x faster                                                        |
| pprint_pformat             | 999 ms                                                      | 922 ms: 1.08x faster                                                        |
| python_startup             | 25.4 ms                                                     | 23.5 ms: 1.08x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 75.2 ms: 1.08x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.46 ms: 1.07x faster                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 50.5 ms: 1.07x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.07x faster                                                       |
| connected_components       | 332 ms                                                      | 312 ms: 1.07x faster                                                        |
| float                      | 49.9 ms                                                     | 47.1 ms: 1.06x faster                                                       |
| shortest_path              | 362 ms                                                      | 347 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.0 ms                                                     | 35.6 ms: 1.04x faster                                                       |
| fannkuch                   | 253 ms                                                      | 244 ms: 1.04x faster                                                        |
| dulwich_log                | 40.8 ms                                                     | 39.6 ms: 1.03x faster                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 204 ms: 1.03x faster                                                        |
| gc_traversal               | 1.97 ms                                                     | 1.92 ms: 1.02x faster                                                       |
| scimark_lu                 | 53.0 ms                                                     | 51.8 ms: 1.02x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 92.8 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.00x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 55.0 ns: 1.01x slower                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 87.1 ms: 1.01x slower                                                       |
| coverage                   | 45.6 ms                                                     | 46.1 ms: 1.01x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.11 us: 1.03x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 75.8 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 395 ms: 1.03x slower                                                        |
| json_dumps                 | 5.92 ms                                                     | 6.12 ms: 1.03x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.52 us: 1.04x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.4 ms: 1.05x slower                                                       |
| go                         | 87.0 ms                                                     | 91.2 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 396 ms: 1.05x slower                                                        |
| pycparser                  | 683 ms                                                      | 720 ms: 1.05x slower                                                        |
| chaos                      | 38.5 ms                                                     | 40.9 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 105 us                                                      | 113 us: 1.07x slower                                                        |
| pyflate                    | 283 ms                                                      | 303 ms: 1.07x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 1.37 ms: 1.09x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 207 us: 1.09x slower                                                        |
| 2to3                       | 221 ms                                                      | 243 ms: 1.10x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 574 ms: 1.11x slower                                                        |
| sympy_expand               | 291 ms                                                      | 323 ms: 1.11x slower                                                        |
| mdp                        | 1.39 sec                                                    | 1.54 sec: 1.11x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 63.2 ms: 1.12x slower                                                       |
| sympy_str                  | 169 ms                                                      | 190 ms: 1.13x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 91.2 ms: 1.13x slower                                                       |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 888 us: 1.15x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 102 ms: 1.17x slower                                                        |
| sqlglot_normalize          | 175 ms                                                      | 207 ms: 1.19x slower                                                        |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                        |
| sphinx                     | 633 ms                                                      | 760 ms: 1.20x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.89 sec: 1.21x slower                                                      |
| django_template            | 22.4 ms                                                     | 27.3 ms: 1.22x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.35 ms: 1.23x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.18 ms: 1.23x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 19.3 ms: 1.24x slower                                                       |
| richards_super             | 30.9 ms                                                     | 38.6 ms: 1.25x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 15.7 ms: 1.25x slower                                                       |
| richards                   | 27.3 ms                                                     | 34.5 ms: 1.26x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 42.5 ms: 1.29x slower                                                       |
| pylint                     | 211 ms                                                      | 275 ms: 1.30x slower                                                        |
| genshi_xml                 | 35.5 ms                                                     | 46.8 ms: 1.32x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 5.20 ms: 1.34x slower                                                       |
| raytrace                   | 160 ms                                                      | 214 ms: 1.34x slower                                                        |
| k_core                     | 1.74 sec                                                    | 2.41 sec: 1.38x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (5): bench_thread_pool, async_tree_io, asyncio_websockets, xml_etree_iterparse, html5lib
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-pythonperf1-amd64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 88.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown