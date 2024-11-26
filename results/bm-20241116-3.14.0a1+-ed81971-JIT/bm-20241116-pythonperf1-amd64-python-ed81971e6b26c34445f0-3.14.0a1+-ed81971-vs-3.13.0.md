# Results vs. 3.13.0

- fork: python
- ref: ed81971e6b26c34445f0
- machine: windows-amd64
- commit hash: ed81971
- commit date: 2024-11-16
- overall geometric mean: 1.002x faster
- HPT reliability: 92.67%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 244 ms: 1.10x slower                                                        |
| docutils       | 1.57 sec                                                    | 1.89 sec: 1.20x slower                                                      |
| sphinx         | 633 ms                                                      | 764 ms: 1.21x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.18x faster                                                        |
| async_tree_none            | 226 ms                                                      | 208 ms: 1.09x faster                                                        |
| async_tree_memoization     | 276 ms                                                      | 263 ms: 1.05x faster                                                        |
| asyncio_websockets         | 318 ms                                                      | 312 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                        |
| async_tree_io              | 521 ms                                                      | 546 ms: 1.05x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.4 ms: 1.05x slower                                                       |
| async_tree_none_tg         | 209 ms                                                      | 221 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.06x slower                                                        |
| async_generators           | 223 ms                                                      | 263 ms: 1.18x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 622 ms: 1.20x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 55.9 ms: 1.22x faster                                                       |
| float          | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                       |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.4 ms: 1.48x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_compile  | 80.5 ms                                                     | 90.3 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.25 sec: 1.12x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 50.7 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 35.7 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 92.6 ms: 1.01x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 141 us: 1.05x slower                                                        |
| json_dumps           | 5.92 ms                                                     | 6.25 ms: 1.06x slower                                                       |
| pickle_pure_python   | 190 us                                                      | 205 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 23.3 ms: 1.09x faster                                                       |
| python_startup_no_site | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.12 ms: 1.24x faster                                                       |
| django_template | 22.4 ms                                                     | 26.8 ms: 1.20x slower                                                       |
| genshi_text     | 15.6 ms                                                     | 19.7 ms: 1.26x slower                                                       |
| genshi_xml      | 35.5 ms                                                     | 47.2 ms: 1.33x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 515 us: 17.10x faster                                                       |
| regex_v8                   | 21.4 ms                                                     | 14.4 ms: 1.48x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 16.1 us: 1.45x faster                                                       |
| mako                       | 6.35 ms                                                     | 5.12 ms: 1.24x faster                                                       |
| nbody                      | 68.4 ms                                                     | 55.9 ms: 1.22x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 51.6 ms: 1.22x faster                                                       |
| deepcopy                   | 226 us                                                      | 187 us: 1.21x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 63.3 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 245 ms: 1.18x faster                                                        |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.14 ms: 1.15x faster                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 39.9 ms: 1.14x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.25 sec: 1.12x faster                                                      |
| scimark_fft                | 172 ms                                                      | 155 ms: 1.11x faster                                                        |
| deepcopy_reduce            | 2.06 us                                                     | 1.86 us: 1.11x faster                                                       |
| telco                      | 4.79 ms                                                     | 4.32 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 40.8 ms                                                     | 37.1 ms: 1.10x faster                                                       |
| json                       | 3.19 ms                                                     | 2.92 ms: 1.09x faster                                                       |
| python_startup             | 25.4 ms                                                     | 23.3 ms: 1.09x faster                                                       |
| async_tree_none            | 226 ms                                                      | 208 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 2.91 sec                                                    | 2.70 sec: 1.08x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 75.0 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 494 ms                                                      | 461 ms: 1.07x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.07x faster                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 50.7 ms: 1.06x faster                                                       |
| pprint_pformat             | 999 ms                                                      | 942 ms: 1.06x faster                                                        |
| connected_components       | 332 ms                                                      | 314 ms: 1.06x faster                                                        |
| float                      | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                       |
| shortest_path              | 362 ms                                                      | 344 ms: 1.05x faster                                                        |
| fannkuch                   | 253 ms                                                      | 241 ms: 1.05x faster                                                        |
| async_tree_memoization     | 276 ms                                                      | 263 ms: 1.05x faster                                                        |
| bench_thread_pool          | 847 us                                                      | 811 us: 1.04x faster                                                        |
| xml_etree_process          | 37.0 ms                                                     | 35.7 ms: 1.04x faster                                                       |
| dulwich_log                | 40.8 ms                                                     | 39.5 ms: 1.03x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.91 ms: 1.03x faster                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                       |
| meteor_contest             | 73.5 ms                                                     | 72.0 ms: 1.02x faster                                                       |
| asyncio_websockets         | 318 ms                                                      | 312 ms: 1.02x faster                                                        |
| scimark_lu                 | 53.0 ms                                                     | 52.3 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 92.6 ms: 1.01x faster                                                       |
| pidigits                   | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 55.0 ns: 1.01x slower                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 87.0 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 391 ms: 1.02x slower                                                        |
| logging_simple             | 5.96 us                                                     | 6.14 us: 1.03x slower                                                       |
| coverage                   | 45.6 ms                                                     | 47.2 ms: 1.04x slower                                                       |
| go                         | 87.0 ms                                                     | 90.2 ms: 1.04x slower                                                       |
| pycparser                  | 683 ms                                                      | 714 ms: 1.05x slower                                                        |
| logging_format             | 6.26 us                                                     | 6.54 us: 1.05x slower                                                       |
| async_tree_io              | 521 ms                                                      | 546 ms: 1.05x slower                                                        |
| coroutines                 | 12.8 ms                                                     | 13.4 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 141 us: 1.05x slower                                                        |
| json_dumps                 | 5.92 ms                                                     | 6.25 ms: 1.06x slower                                                       |
| async_tree_none_tg         | 209 ms                                                      | 221 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 401 ms: 1.06x slower                                                        |
| chaos                      | 38.5 ms                                                     | 41.3 ms: 1.07x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 205 us: 1.08x slower                                                        |
| sympy_expand               | 291 ms                                                      | 318 ms: 1.09x slower                                                        |
| 2to3                       | 221 ms                                                      | 244 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 116 us: 1.10x slower                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 1.39 ms: 1.10x slower                                                       |
| sympy_str                  | 169 ms                                                      | 188 ms: 1.11x slower                                                        |
| regex_compile              | 80.5 ms                                                     | 90.3 ms: 1.12x slower                                                       |
| pyflate                    | 283 ms                                                      | 321 ms: 1.13x slower                                                        |
| sqlglot_parse              | 771 us                                                      | 880 us: 1.14x slower                                                        |
| nqueens                    | 56.7 ms                                                     | 65.3 ms: 1.15x slower                                                       |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 101 ms: 1.16x slower                                                        |
| generators                 | 19.5 ms                                                     | 22.8 ms: 1.17x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.63 sec: 1.17x slower                                                      |
| async_generators           | 223 ms                                                      | 263 ms: 1.18x slower                                                        |
| sqlglot_normalize          | 175 ms                                                      | 208 ms: 1.19x slower                                                        |
| django_template            | 22.4 ms                                                     | 26.8 ms: 1.20x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 622 ms: 1.20x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.89 sec: 1.20x slower                                                      |
| sphinx                     | 633 ms                                                      | 764 ms: 1.21x slower                                                        |
| sqlglot_transpile          | 956 us                                                      | 1.16 ms: 1.21x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.33 ms: 1.22x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 15.4 ms: 1.23x slower                                                       |
| richards_super             | 30.9 ms                                                     | 38.5 ms: 1.25x slower                                                       |
| richards                   | 27.3 ms                                                     | 34.2 ms: 1.25x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 19.7 ms: 1.26x slower                                                       |
| pylint                     | 211 ms                                                      | 274 ms: 1.30x slower                                                        |
| sqlglot_optimize           | 32.9 ms                                                     | 42.9 ms: 1.30x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 5.18 ms: 1.33x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 47.2 ms: 1.33x slower                                                       |
| raytrace                   | 160 ms                                                      | 221 ms: 1.38x slower                                                        |
| k_core                     | 1.74 sec                                                    | 2.42 sec: 1.39x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (3): html5lib, regex_effbot, xml_etree_iterparse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (3) of results/bm-20241116-3.14.0a1+-ed81971-JIT/bm-20241116-pythonperf1-amd64-python-ed81971e6b26c34445f0-3.14.0a1+-ed81971.json: many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 92.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown