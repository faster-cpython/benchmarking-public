# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: windows-amd64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.022x faster
- HPT reliability: 96.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 240 ms: 1.09x slower                                                 |
| docutils       | 1.57 sec                                                    | 1.84 sec: 1.17x slower                                               |
| sphinx         | 633 ms                                                      | 743 ms: 1.17x slower                                                 |
| tornado_http   | 93.0 ms                                                     | 98.0 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                       | 1.09x slower                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                 |
| async_tree_none            | 226 ms                                                      | 218 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                 |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.08x slower                                                |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                 |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                 |
| async_tree_io_tg           | 518 ms                                                      | 631 ms: 1.22x slower                                                 |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                         |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 53.1 ms: 1.29x faster                                                |
| float          | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                |
| pidigits       | 148 ms                                                      | 148 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                       | 1.10x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                |
| regex_effbot   | 1.58 ms                                                     | 1.66 ms: 1.06x slower                                                |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                 |
| regex_compile  | 80.5 ms                                                     | 86.7 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                       | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.24 sec: 1.12x faster                                               |
| xml_etree_generate   | 54.0 ms                                                     | 50.2 ms: 1.08x faster                                                |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                |
| xml_etree_process    | 37.0 ms                                                     | 36.0 ms: 1.03x faster                                                |
| xml_etree_parse      | 93.6 ms                                                     | 95.5 ms: 1.02x slower                                                |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.7 ms: 1.03x slower                                                |
| pickle_pure_python   | 190 us                                                      | 199 us: 1.05x slower                                                 |
| json_dumps           | 5.92 ms                                                     | 6.27 ms: 1.06x slower                                                |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.2 ms: 1.05x faster                                                |
| python_startup_no_site | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.08 ms: 1.25x faster                                                |
| genshi_xml      | 35.5 ms                                                     | 38.0 ms: 1.07x slower                                                |
| django_template | 22.4 ms                                                     | 25.3 ms: 1.13x slower                                                |
| genshi_text     | 15.6 ms                                                     | 17.9 ms: 1.15x slower                                                |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1-amd64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 519 us: 16.95x faster                                                |
| deepcopy_memo              | 23.3 us                                                     | 15.8 us: 1.47x faster                                                |
| regex_v8                   | 21.4 ms                                                     | 15.5 ms: 1.38x faster                                                |
| nbody                      | 68.4 ms                                                     | 53.1 ms: 1.29x faster                                                |
| mako                       | 6.35 ms                                                     | 5.08 ms: 1.25x faster                                                |
| deepcopy                   | 226 us                                                      | 183 us: 1.24x faster                                                 |
| scimark_sor                | 76.2 ms                                                     | 63.7 ms: 1.20x faster                                                |
| fannkuch                   | 253 ms                                                      | 212 ms: 1.19x faster                                                 |
| deepcopy_reduce            | 2.06 us                                                     | 1.80 us: 1.14x faster                                                |
| crypto_pyaes               | 45.4 ms                                                     | 39.9 ms: 1.14x faster                                                |
| pprint_safe_repr           | 494 ms                                                      | 433 ms: 1.14x faster                                                 |
| scimark_monte_carlo        | 40.8 ms                                                     | 36.1 ms: 1.13x faster                                                |
| spectral_norm              | 62.8 ms                                                     | 55.7 ms: 1.13x faster                                                |
| tomli_loads                | 1.39 sec                                                    | 1.24 sec: 1.12x faster                                               |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.21 ms: 1.11x faster                                                |
| async_tree_memoization_tg  | 288 ms                                                      | 260 ms: 1.11x faster                                                 |
| pprint_pformat             | 999 ms                                                      | 906 ms: 1.10x faster                                                 |
| scimark_fft                | 172 ms                                                      | 157 ms: 1.10x faster                                                 |
| json                       | 3.19 ms                                                     | 2.94 ms: 1.08x faster                                                |
| xml_etree_generate         | 54.0 ms                                                     | 50.2 ms: 1.08x faster                                                |
| go                         | 87.0 ms                                                     | 82.2 ms: 1.06x faster                                                |
| float                      | 49.9 ms                                                     | 47.4 ms: 1.05x faster                                                |
| python_startup             | 25.4 ms                                                     | 24.2 ms: 1.05x faster                                                |
| telco                      | 4.79 ms                                                     | 4.57 ms: 1.05x faster                                                |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                |
| async_tree_none            | 226 ms                                                      | 218 ms: 1.04x faster                                                 |
| pyflate                    | 283 ms                                                      | 274 ms: 1.03x faster                                                 |
| xml_etree_process          | 37.0 ms                                                     | 36.0 ms: 1.03x faster                                                |
| dulwich_log                | 40.8 ms                                                     | 39.9 ms: 1.02x faster                                                |
| meteor_contest             | 73.5 ms                                                     | 71.9 ms: 1.02x faster                                                |
| gc_traversal               | 1.97 ms                                                     | 1.94 ms: 1.01x faster                                                |
| pathlib                    | 80.9 ms                                                     | 80.3 ms: 1.01x faster                                                |
| pidigits                   | 148 ms                                                      | 148 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 389 ms: 1.01x slower                                                 |
| logging_simple             | 5.96 us                                                     | 6.05 us: 1.02x slower                                                |
| pycparser                  | 683 ms                                                      | 696 ms: 1.02x slower                                                 |
| xml_etree_parse            | 93.6 ms                                                     | 95.5 ms: 1.02x slower                                                |
| scimark_lu                 | 53.0 ms                                                     | 54.1 ms: 1.02x slower                                                |
| python_startup_no_site     | 18.1 ms                                                     | 18.5 ms: 1.02x slower                                                |
| chaos                      | 38.5 ms                                                     | 39.5 ms: 1.02x slower                                                |
| sympy_expand               | 291 ms                                                      | 300 ms: 1.03x slower                                                 |
| logging_format             | 6.26 us                                                     | 6.44 us: 1.03x slower                                                |
| bench_mp_pool              | 86.4 ms                                                     | 89.1 ms: 1.03x slower                                                |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.7 ms: 1.03x slower                                                |
| pickle_pure_python         | 190 us                                                      | 199 us: 1.05x slower                                                 |
| coverage                   | 45.6 ms                                                     | 47.8 ms: 1.05x slower                                                |
| tornado_http               | 93.0 ms                                                     | 98.0 ms: 1.05x slower                                                |
| regex_effbot               | 1.58 ms                                                     | 1.66 ms: 1.06x slower                                                |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 399 ms: 1.06x slower                                                 |
| json_dumps                 | 5.92 ms                                                     | 6.27 ms: 1.06x slower                                                |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                 |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                 |
| comprehensions             | 10.3 us                                                     | 10.9 us: 1.06x slower                                                |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.07x slower                                                 |
| genshi_xml                 | 35.5 ms                                                     | 38.0 ms: 1.07x slower                                                |
| regex_compile              | 80.5 ms                                                     | 86.7 ms: 1.08x slower                                                |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.08x slower                                                 |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.08x slower                                                |
| 2to3                       | 221 ms                                                      | 240 ms: 1.09x slower                                                 |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                 |
| mdp                        | 1.39 sec                                                    | 1.53 sec: 1.10x slower                                               |
| hexiom                     | 3.89 ms                                                     | 4.28 ms: 1.10x slower                                                |
| sqlglot_parse              | 771 us                                                      | 850 us: 1.10x slower                                                 |
| nqueens                    | 56.7 ms                                                     | 62.7 ms: 1.11x slower                                                |
| create_gc_cycles           | 1.26 ms                                                     | 1.39 ms: 1.11x slower                                                |
| sqlglot_normalize          | 175 ms                                                      | 194 ms: 1.11x slower                                                 |
| generators                 | 19.5 ms                                                     | 21.6 ms: 1.11x slower                                                |
| sympy_sum                  | 86.9 ms                                                     | 98.0 ms: 1.13x slower                                                |
| richards                   | 27.3 ms                                                     | 30.8 ms: 1.13x slower                                                |
| django_template            | 22.4 ms                                                     | 25.3 ms: 1.13x slower                                                |
| richards_super             | 30.9 ms                                                     | 35.0 ms: 1.13x slower                                                |
| genshi_text                | 15.6 ms                                                     | 17.9 ms: 1.15x slower                                                |
| deltablue                  | 1.92 ms                                                     | 2.23 ms: 1.16x slower                                                |
| sqlglot_transpile          | 956 us                                                      | 1.11 ms: 1.16x slower                                                |
| docutils                   | 1.57 sec                                                    | 1.84 sec: 1.17x slower                                               |
| sphinx                     | 633 ms                                                      | 743 ms: 1.17x slower                                                 |
| async_generators           | 223 ms                                                      | 264 ms: 1.18x slower                                                 |
| sqlglot_optimize           | 32.9 ms                                                     | 39.4 ms: 1.20x slower                                                |
| sympy_integrate            | 12.5 ms                                                     | 15.0 ms: 1.20x slower                                                |
| async_tree_io_tg           | 518 ms                                                      | 631 ms: 1.22x slower                                                 |
| raytrace                   | 160 ms                                                      | 200 ms: 1.25x slower                                                 |
| pylint                     | 211 ms                                                      | 268 ms: 1.27x slower                                                 |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                         |

Benchmark hidden because not significant (5): html5lib, logging_silent, bench_thread_pool, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.022x faster
# HPT report

- Reliability score: 96.90% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown