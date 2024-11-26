# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.030x faster
- HPT reliability: 97.49%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 240 ms: 1.08x slower                                             |
| docutils       | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                           |
| html5lib       | 38.9 ms                                                     | 41.4 ms: 1.06x slower                                            |
| tornado_http   | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                            |
| Geometric mean | (ref)                                                       | 1.08x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                             |
| async_tree_none            | 226 ms                                                      | 202 ms: 1.12x faster                                             |
| async_tree_memoization     | 276 ms                                                      | 255 ms: 1.08x faster                                             |
| async_tree_none_tg         | 209 ms                                                      | 197 ms: 1.06x faster                                             |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 393 ms: 1.03x slower                                             |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 396 ms: 1.05x slower                                             |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 556 ms: 1.07x slower                                             |
| async_tree_io              | 521 ms                                                      | 578 ms: 1.11x slower                                             |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                             |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 49.6 ms: 1.38x faster                                            |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                             |
| float          | 49.9 ms                                                     | 53.4 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                       | 1.08x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.8 ms: 1.44x faster                                            |
| regex_effbot   | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                            |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                             |
| regex_compile  | 80.5 ms                                                     | 94.7 ms: 1.18x slower                                            |
| Geometric mean | (ref)                                                       | 1.04x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.29 sec: 1.08x faster                                           |
| xml_etree_process    | 37.0 ms                                                     | 34.8 ms: 1.06x faster                                            |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                            |
| xml_etree_generate   | 54.0 ms                                                     | 51.7 ms: 1.04x faster                                            |
| xml_etree_iterparse  | 61.8 ms                                                     | 59.8 ms: 1.03x faster                                            |
| xml_etree_parse      | 93.6 ms                                                     | 92.1 ms: 1.02x faster                                            |
| pickle_pure_python   | 190 us                                                      | 196 us: 1.03x slower                                             |
| unpickle_pure_python | 133 us                                                      | 143 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                            |
| Geometric mean | (ref)                                                       | 1.07x faster                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.20 ms: 1.22x faster                                            |
| django_template | 22.4 ms                                                     | 26.4 ms: 1.18x slower                                            |
| genshi_text     | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                            |
| genshi_xml      | 35.5 ms                                                     | 45.5 ms: 1.28x slower                                            |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 516 us: 17.05x faster                                            |
| deepcopy_memo              | 23.3 us                                                     | 15.3 us: 1.53x faster                                            |
| regex_v8                   | 21.4 ms                                                     | 14.8 ms: 1.44x faster                                            |
| create_gc_cycles           | 1.26 ms                                                     | 895 us: 1.41x faster                                             |
| spectral_norm              | 62.8 ms                                                     | 44.8 ms: 1.40x faster                                            |
| nbody                      | 68.4 ms                                                     | 49.6 ms: 1.38x faster                                            |
| gc_traversal               | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                            |
| scimark_sor                | 76.2 ms                                                     | 60.5 ms: 1.26x faster                                            |
| deepcopy                   | 226 us                                                      | 183 us: 1.23x faster                                             |
| bench_mp_pool              | 86.4 ms                                                     | 70.2 ms: 1.23x faster                                            |
| mako                       | 6.35 ms                                                     | 5.20 ms: 1.22x faster                                            |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.06 ms: 1.19x faster                                            |
| crypto_pyaes               | 45.4 ms                                                     | 38.1 ms: 1.19x faster                                            |
| scimark_fft                | 172 ms                                                      | 147 ms: 1.17x faster                                             |
| python_startup             | 25.4 ms                                                     | 22.2 ms: 1.15x faster                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                             |
| deepcopy_reduce            | 2.06 us                                                     | 1.83 us: 1.12x faster                                            |
| async_tree_none            | 226 ms                                                      | 202 ms: 1.12x faster                                             |
| json                       | 3.19 ms                                                     | 2.90 ms: 1.10x faster                                            |
| fannkuch                   | 253 ms                                                      | 233 ms: 1.09x faster                                             |
| async_tree_memoization     | 276 ms                                                      | 255 ms: 1.08x faster                                             |
| pyflate                    | 283 ms                                                      | 263 ms: 1.08x faster                                             |
| tomli_loads                | 1.39 sec                                                    | 1.29 sec: 1.08x faster                                           |
| pathlib                    | 80.9 ms                                                     | 75.6 ms: 1.07x faster                                            |
| xml_etree_process          | 37.0 ms                                                     | 34.8 ms: 1.06x faster                                            |
| telco                      | 4.79 ms                                                     | 4.53 ms: 1.06x faster                                            |
| async_tree_none_tg         | 209 ms                                                      | 197 ms: 1.06x faster                                             |
| tornado_http               | 93.0 ms                                                     | 88.1 ms: 1.06x faster                                            |
| deltablue                  | 1.92 ms                                                     | 1.83 ms: 1.05x faster                                            |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                            |
| xml_etree_generate         | 54.0 ms                                                     | 51.7 ms: 1.04x faster                                            |
| xml_etree_iterparse        | 61.8 ms                                                     | 59.8 ms: 1.03x faster                                            |
| xml_etree_parse            | 93.6 ms                                                     | 92.1 ms: 1.02x faster                                            |
| logging_simple             | 5.96 us                                                     | 5.91 us: 1.01x faster                                            |
| logging_format             | 6.26 us                                                     | 6.33 us: 1.01x slower                                            |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                             |
| coverage                   | 45.6 ms                                                     | 46.5 ms: 1.02x slower                                            |
| comprehensions             | 10.3 us                                                     | 10.5 us: 1.02x slower                                            |
| regex_effbot               | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                            |
| meteor_contest             | 73.5 ms                                                     | 75.3 ms: 1.02x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 393 ms: 1.03x slower                                             |
| dulwich_log                | 40.8 ms                                                     | 42.0 ms: 1.03x slower                                            |
| pickle_pure_python         | 190 us                                                      | 196 us: 1.03x slower                                             |
| pycparser                  | 683 ms                                                      | 706 ms: 1.03x slower                                             |
| logging_silent             | 54.6 ns                                                     | 57.0 ns: 1.04x slower                                            |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                             |
| scimark_monte_carlo        | 40.8 ms                                                     | 42.7 ms: 1.05x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 396 ms: 1.05x slower                                             |
| go                         | 87.0 ms                                                     | 91.7 ms: 1.05x slower                                            |
| chaos                      | 38.5 ms                                                     | 40.7 ms: 1.06x slower                                            |
| typing_runtime_protocols   | 105 us                                                      | 112 us: 1.06x slower                                             |
| pprint_safe_repr           | 494 ms                                                      | 524 ms: 1.06x slower                                             |
| nqueens                    | 56.7 ms                                                     | 60.2 ms: 1.06x slower                                            |
| html5lib                   | 38.9 ms                                                     | 41.4 ms: 1.06x slower                                            |
| float                      | 49.9 ms                                                     | 53.4 ms: 1.07x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 556 ms: 1.07x slower                                             |
| unpickle_pure_python       | 133 us                                                      | 143 us: 1.07x slower                                             |
| pprint_pformat             | 999 ms                                                      | 1.07 sec: 1.07x slower                                           |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                           |
| 2to3                       | 221 ms                                                      | 240 ms: 1.08x slower                                             |
| async_tree_io              | 521 ms                                                      | 578 ms: 1.11x slower                                             |
| sympy_str                  | 169 ms                                                      | 189 ms: 1.12x slower                                             |
| generators                 | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                            |
| sqlglot_normalize          | 175 ms                                                      | 198 ms: 1.14x slower                                             |
| sympy_expand               | 291 ms                                                      | 332 ms: 1.14x slower                                             |
| sympy_sum                  | 86.9 ms                                                     | 99.1 ms: 1.14x slower                                            |
| sqlglot_parse              | 771 us                                                      | 887 us: 1.15x slower                                             |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                             |
| regex_compile              | 80.5 ms                                                     | 94.7 ms: 1.18x slower                                            |
| django_template            | 22.4 ms                                                     | 26.4 ms: 1.18x slower                                            |
| sympy_integrate            | 12.5 ms                                                     | 14.9 ms: 1.19x slower                                            |
| sqlglot_optimize           | 32.9 ms                                                     | 39.7 ms: 1.20x slower                                            |
| sqlglot_transpile          | 956 us                                                      | 1.16 ms: 1.21x slower                                            |
| docutils                   | 1.57 sec                                                    | 1.93 sec: 1.23x slower                                           |
| genshi_text                | 15.6 ms                                                     | 19.2 ms: 1.23x slower                                            |
| raytrace                   | 160 ms                                                      | 198 ms: 1.24x slower                                             |
| pylint                     | 211 ms                                                      | 264 ms: 1.25x slower                                             |
| hexiom                     | 3.89 ms                                                     | 4.88 ms: 1.26x slower                                            |
| richards_super             | 30.9 ms                                                     | 39.3 ms: 1.27x slower                                            |
| genshi_xml                 | 35.5 ms                                                     | 45.5 ms: 1.28x slower                                            |
| richards                   | 27.3 ms                                                     | 36.6 ms: 1.34x slower                                            |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                     |

Benchmark hidden because not significant (4): bench_thread_pool, json_dumps, python_startup_no_site, scimark_lu
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 97.49% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown