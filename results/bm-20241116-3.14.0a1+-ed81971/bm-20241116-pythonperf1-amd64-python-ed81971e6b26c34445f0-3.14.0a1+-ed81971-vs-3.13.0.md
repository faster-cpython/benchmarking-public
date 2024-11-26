# Results vs. 3.13.0

- fork: python
- ref: ed81971e6b26c34445f0
- machine: windows-amd64
- commit hash: ed81971
- commit date: 2024-11-16
- overall geometric mean: 1.039x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 224 ms: 1.01x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                      |
| html5lib       | 38.9 ms                                                     | 40.2 ms: 1.03x slower                                                       |
| sphinx         | 633 ms                                                      | 671 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                        |
| async_tree_io              | 521 ms                                                      | 558 ms: 1.07x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 628 ms: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (5): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 145 ms: 1.02x faster                                                        |
| float          | 49.9 ms                                                     | 56.4 ms: 1.13x slower                                                       |
| nbody          | 68.4 ms                                                     | 82.8 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 91.2 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 96.8 ms: 1.03x slower                                                       |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.9 ms: 1.07x slower                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 59.2 ms: 1.10x slower                                                       |
| xml_etree_process    | 37.0 ms                                                     | 41.2 ms: 1.11x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.66 ms: 1.13x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                        |
| pickle_pure_python   | 190 us                                                      | 227 us: 1.20x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.0 ms: 1.06x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.9 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 37.2 ms: 1.05x slower                                                       |
| mako            | 6.35 ms                                                     | 6.95 ms: 1.09x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| django_template | 22.4 ms                                                     | 25.4 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 528 us: 16.65x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 15.2 ms: 1.41x faster                                                       |
| deepcopy                   | 226 us                                                      | 194 us: 1.17x faster                                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                        |
| deepcopy_memo              | 23.3 us                                                     | 21.3 us: 1.10x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 74.5 ms: 1.09x faster                                                       |
| python_startup             | 25.4 ms                                                     | 24.0 ms: 1.06x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 82.0 ms: 1.05x faster                                                       |
| json                       | 3.19 ms                                                     | 3.03 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.98 us: 1.04x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.91 ms: 1.03x faster                                                       |
| connected_components       | 332 ms                                                      | 326 ms: 1.02x faster                                                        |
| pidigits                   | 148 ms                                                      | 145 ms: 1.02x faster                                                        |
| shortest_path              | 362 ms                                                      | 357 ms: 1.01x faster                                                        |
| python_startup_no_site     | 18.1 ms                                                     | 17.9 ms: 1.01x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                       |
| 2to3                       | 221 ms                                                      | 224 ms: 1.01x slower                                                        |
| coverage                   | 45.6 ms                                                     | 46.3 ms: 1.02x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.2 ms: 1.03x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 89.7 ms: 1.03x slower                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 96.8 ms: 1.03x slower                                                       |
| go                         | 87.0 ms                                                     | 90.2 ms: 1.04x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 37.2 ms: 1.05x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 42.9 ms: 1.05x slower                                                       |
| bpe_tokeniser              | 2.91 sec                                                    | 3.08 sec: 1.06x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 48.1 ms: 1.06x slower                                                       |
| sympy_expand               | 291 ms                                                      | 309 ms: 1.06x slower                                                        |
| sphinx                     | 633 ms                                                      | 671 ms: 1.06x slower                                                        |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 112 us: 1.07x slower                                                        |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.9 ms: 1.07x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 402 ms: 1.07x slower                                                        |
| async_tree_io              | 521 ms                                                      | 558 ms: 1.07x slower                                                        |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.07x slower                                                        |
| logging_simple             | 5.96 us                                                     | 6.39 us: 1.07x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.08x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 79.3 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| spectral_norm              | 62.8 ms                                                     | 67.8 ms: 1.08x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                      |
| pycparser                  | 683 ms                                                      | 741 ms: 1.08x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.82 us: 1.09x slower                                                       |
| mako                       | 6.35 ms                                                     | 6.95 ms: 1.09x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 59.2 ms: 1.10x slower                                                       |
| create_gc_cycles           | 1.26 ms                                                     | 1.38 ms: 1.10x slower                                                       |
| fannkuch                   | 253 ms                                                      | 278 ms: 1.10x slower                                                        |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                        |
| xml_etree_process          | 37.0 ms                                                     | 41.2 ms: 1.11x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 63.3 ms: 1.12x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                       |
| json_dumps                 | 5.92 ms                                                     | 6.66 ms: 1.13x slower                                                       |
| chaos                      | 38.5 ms                                                     | 43.4 ms: 1.13x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 37.1 ms: 1.13x slower                                                       |
| float                      | 49.9 ms                                                     | 56.4 ms: 1.13x slower                                                       |
| pprint_safe_repr           | 494 ms                                                      | 558 ms: 1.13x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 91.2 ms: 1.13x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                                      |
| pyflate                    | 283 ms                                                      | 321 ms: 1.13x slower                                                        |
| django_template            | 22.4 ms                                                     | 25.4 ms: 1.14x slower                                                       |
| sqlglot_normalize          | 175 ms                                                      | 200 ms: 1.14x slower                                                        |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.81 ms: 1.15x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.51 ms: 1.16x slower                                                       |
| scimark_fft                | 172 ms                                                      | 200 ms: 1.16x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 47.7 ms: 1.17x slower                                                       |
| richards_super             | 30.9 ms                                                     | 36.4 ms: 1.18x slower                                                       |
| richards                   | 27.3 ms                                                     | 32.5 ms: 1.19x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.29 ms: 1.19x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 227 us: 1.20x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 91.2 ms: 1.20x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.15 ms: 1.20x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 65.5 ns: 1.20x slower                                                       |
| comprehensions             | 10.3 us                                                     | 12.4 us: 1.21x slower                                                       |
| nbody                      | 68.4 ms                                                     | 82.8 ms: 1.21x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 933 us: 1.21x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 628 ms: 1.21x slower                                                        |
| scimark_lu                 | 53.0 ms                                                     | 64.9 ms: 1.22x slower                                                       |
| raytrace                   | 160 ms                                                      | 197 ms: 1.23x slower                                                        |
| k_core                     | 1.74 sec                                                    | 2.53 sec: 1.46x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (8): bench_thread_pool, async_tree_none, async_tree_memoization, telco, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241116-3.14.0a1+-ed81971/bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.039x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown