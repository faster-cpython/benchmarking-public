# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.305x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 222 ms                                                                     | 295 ms: 1.33x slower                                                       |
| docutils       | 1.62 sec                                                                   | 2.08 sec: 1.28x slower                                                     |
| html5lib       | 39.0 ms                                                                    | 51.5 ms: 1.32x slower                                                      |
| sphinx         | 639 ms                                                                     | 838 ms: 1.31x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.31x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 157 ms                                                                     | 161 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 340 ms                                                                     | 438 ms: 1.29x slower                                                       |
| async_tree_cpu_io_mixed    | 330 ms                                                                     | 440 ms: 1.33x slower                                                       |
| async_tree_io              | 400 ms                                                                     | 546 ms: 1.36x slower                                                       |
| async_tree_none_tg         | 170 ms                                                                     | 235 ms: 1.39x slower                                                       |
| async_tree_memoization_tg  | 211 ms                                                                     | 292 ms: 1.39x slower                                                       |
| async_tree_none            | 174 ms                                                                     | 242 ms: 1.40x slower                                                       |
| async_tree_memoization     | 209 ms                                                                     | 295 ms: 1.41x slower                                                       |
| async_tree_io_tg           | 395 ms                                                                     | 561 ms: 1.42x slower                                                       |
| async_generators           | 231 ms                                                                     | 332 ms: 1.44x slower                                                       |
| coroutines                 | 14.1 ms                                                                    | 24.7 ms: 1.75x slower                                                      |
| Geometric mean             | (ref)                                                                      | 1.37x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 61.8 ms                                                                    | 99.6 ms: 1.61x slower                                                      |
| float          | 44.1 ms                                                                    | 76.0 ms: 1.72x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.41x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                     | 117 ms: 1.04x faster                                                       |
| regex_effbot   | 1.61 ms                                                                    | 1.73 ms: 1.07x slower                                                      |
| regex_v8       | 14.0 ms                                                                    | 17.0 ms: 1.21x slower                                                      |
| regex_compile  | 78.9 ms                                                                    | 122 ms: 1.54x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.18x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 88.5 ms                                                                    | 108 ms: 1.22x slower                                                       |
| xml_etree_iterparse  | 64.4 ms                                                                    | 89.5 ms: 1.39x slower                                                      |
| json_dumps           | 6.24 ms                                                                    | 8.83 ms: 1.42x slower                                                      |
| tomli_loads          | 1.37 sec                                                                   | 2.02 sec: 1.48x slower                                                     |
| json_loads           | 14.2 us                                                                    | 21.1 us: 1.49x slower                                                      |
| xml_etree_generate   | 56.2 ms                                                                    | 89.3 ms: 1.59x slower                                                      |
| xml_etree_process    | 39.3 ms                                                                    | 64.0 ms: 1.63x slower                                                      |
| pickle_pure_python   | 207 us                                                                     | 358 us: 1.73x slower                                                       |
| unpickle_pure_python | 133 us                                                                     | 275 us: 2.06x slower                                                       |
| Geometric mean       | (ref)                                                                      | 1.54x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 19.4 ms                                                                    | 20.0 ms: 1.03x slower                                                      |
| python_startup         | 25.8 ms                                                                    | 27.2 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                                      | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 34.3 ms                                                                    | 48.3 ms: 1.41x slower                                                      |
| django_template | 24.1 ms                                                                    | 36.3 ms: 1.50x slower                                                      |
| genshi_text     | 15.4 ms                                                                    | 23.3 ms: 1.51x slower                                                      |
| mako            | 6.73 ms                                                                    | 12.4 ms: 1.84x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.56x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna                  | 122 ms                                                                     | 117 ms: 1.04x faster                                                       |
| asyncio_websockets         | 157 ms                                                                     | 161 ms: 1.02x slower                                                       |
| python_startup_no_site     | 19.4 ms                                                                    | 20.0 ms: 1.03x slower                                                      |
| connected_components       | 336 ms                                                                     | 347 ms: 1.03x slower                                                       |
| python_startup             | 25.8 ms                                                                    | 27.2 ms: 1.05x slower                                                      |
| k_core                     | 1.70 sec                                                                   | 1.81 sec: 1.06x slower                                                     |
| pathlib                    | 32.1 ms                                                                    | 34.3 ms: 1.07x slower                                                      |
| regex_effbot               | 1.61 ms                                                                    | 1.73 ms: 1.07x slower                                                      |
| create_gc_cycles           | 1.34 ms                                                                    | 1.48 ms: 1.10x slower                                                      |
| sqlite_synth               | 1.59 us                                                                    | 1.86 us: 1.17x slower                                                      |
| regex_v8                   | 14.0 ms                                                                    | 17.0 ms: 1.21x slower                                                      |
| xml_etree_parse            | 88.5 ms                                                                    | 108 ms: 1.22x slower                                                       |
| dulwich_log                | 41.3 ms                                                                    | 50.8 ms: 1.23x slower                                                      |
| pylint                     | 198 ms                                                                     | 247 ms: 1.25x slower                                                       |
| many_optionals             | 434 us                                                                     | 547 us: 1.26x slower                                                       |
| coverage                   | 49.0 ms                                                                    | 62.3 ms: 1.27x slower                                                      |
| meteor_contest             | 72.5 ms                                                                    | 92.3 ms: 1.27x slower                                                      |
| docutils                   | 1.62 sec                                                                   | 2.08 sec: 1.28x slower                                                     |
| async_tree_cpu_io_mixed_tg | 340 ms                                                                     | 438 ms: 1.29x slower                                                       |
| sphinx                     | 639 ms                                                                     | 838 ms: 1.31x slower                                                       |
| sympy_sum                  | 87.2 ms                                                                    | 115 ms: 1.31x slower                                                       |
| subparsers                 | 17.0 ms                                                                    | 22.3 ms: 1.32x slower                                                      |
| html5lib                   | 39.0 ms                                                                    | 51.5 ms: 1.32x slower                                                      |
| sympy_integrate            | 12.4 ms                                                                    | 16.4 ms: 1.33x slower                                                      |
| 2to3                       | 222 ms                                                                     | 295 ms: 1.33x slower                                                       |
| async_tree_cpu_io_mixed    | 330 ms                                                                     | 440 ms: 1.33x slower                                                       |
| async_tree_io              | 400 ms                                                                     | 546 ms: 1.36x slower                                                       |
| telco                      | 4.55 ms                                                                    | 6.25 ms: 1.37x slower                                                      |
| pycparser                  | 710 ms                                                                     | 974 ms: 1.37x slower                                                       |
| sympy_str                  | 168 ms                                                                     | 231 ms: 1.37x slower                                                       |
| sympy_expand               | 286 ms                                                                     | 396 ms: 1.38x slower                                                       |
| thrift                     | 500 us                                                                     | 692 us: 1.38x slower                                                       |
| async_tree_none_tg         | 170 ms                                                                     | 235 ms: 1.39x slower                                                       |
| async_tree_memoization_tg  | 211 ms                                                                     | 292 ms: 1.39x slower                                                       |
| xml_etree_iterparse        | 64.4 ms                                                                    | 89.5 ms: 1.39x slower                                                      |
| async_tree_none            | 174 ms                                                                     | 242 ms: 1.40x slower                                                       |
| json                       | 2.97 ms                                                                    | 4.17 ms: 1.40x slower                                                      |
| genshi_xml                 | 34.3 ms                                                                    | 48.3 ms: 1.41x slower                                                      |
| gc_traversal               | 2.17 ms                                                                    | 3.05 ms: 1.41x slower                                                      |
| async_tree_memoization     | 209 ms                                                                     | 295 ms: 1.41x slower                                                       |
| json_dumps                 | 6.24 ms                                                                    | 8.83 ms: 1.42x slower                                                      |
| async_tree_io_tg           | 395 ms                                                                     | 561 ms: 1.42x slower                                                       |
| mdp                        | 800 ms                                                                     | 1.15 sec: 1.44x slower                                                     |
| async_generators           | 231 ms                                                                     | 332 ms: 1.44x slower                                                       |
| logging_format             | 6.77 us                                                                    | 9.74 us: 1.44x slower                                                      |
| bpe_tokeniser              | 2.97 sec                                                                   | 4.28 sec: 1.44x slower                                                     |
| logging_silent             | 342 ns                                                                     | 494 ns: 1.44x slower                                                       |
| deepcopy_reduce            | 1.86 us                                                                    | 2.71 us: 1.46x slower                                                      |
| logging_simple             | 6.28 us                                                                    | 9.25 us: 1.47x slower                                                      |
| sqlglot_v2_optimize        | 33.7 ms                                                                    | 49.8 ms: 1.48x slower                                                      |
| tomli_loads                | 1.37 sec                                                                   | 2.02 sec: 1.48x slower                                                     |
| sqlglot_v2_normalize       | 69.7 ms                                                                    | 104 ms: 1.48x slower                                                       |
| json_loads                 | 14.2 us                                                                    | 21.1 us: 1.49x slower                                                      |
| nqueens                    | 60.9 ms                                                                    | 91.5 ms: 1.50x slower                                                      |
| django_template            | 24.1 ms                                                                    | 36.3 ms: 1.50x slower                                                      |
| genshi_text                | 15.4 ms                                                                    | 23.3 ms: 1.51x slower                                                      |
| typing_runtime_protocols   | 101 us                                                                     | 153 us: 1.52x slower                                                       |
| scimark_fft                | 172 ms                                                                     | 265 ms: 1.54x slower                                                       |
| deepcopy                   | 170 us                                                                     | 262 us: 1.54x slower                                                       |
| regex_compile              | 78.9 ms                                                                    | 122 ms: 1.54x slower                                                       |
| pyflate                    | 289 ms                                                                     | 453 ms: 1.57x slower                                                       |
| fannkuch                   | 257 ms                                                                     | 406 ms: 1.58x slower                                                       |
| sqlglot_v2_transpile       | 1.02 ms                                                                    | 1.61 ms: 1.58x slower                                                      |
| xml_etree_generate         | 56.2 ms                                                                    | 89.3 ms: 1.59x slower                                                      |
| pprint_safe_repr           | 537 ms                                                                     | 854 ms: 1.59x slower                                                       |
| pprint_pformat             | 1.09 sec                                                                   | 1.74 sec: 1.59x slower                                                     |
| chaos                      | 39.9 ms                                                                    | 64.0 ms: 1.60x slower                                                      |
| nbody                      | 61.8 ms                                                                    | 99.6 ms: 1.61x slower                                                      |
| xml_etree_process          | 39.3 ms                                                                    | 64.0 ms: 1.63x slower                                                      |
| sqlglot_v2_parse           | 822 us                                                                     | 1.34 ms: 1.64x slower                                                      |
| scimark_sparse_mat_mult    | 2.52 ms                                                                    | 4.16 ms: 1.65x slower                                                      |
| crypto_pyaes               | 47.1 ms                                                                    | 79.7 ms: 1.69x slower                                                      |
| raytrace                   | 177 ms                                                                     | 300 ms: 1.70x slower                                                       |
| float                      | 44.1 ms                                                                    | 76.0 ms: 1.72x slower                                                      |
| scimark_sor                | 75.0 ms                                                                    | 130 ms: 1.73x slower                                                       |
| pickle_pure_python         | 207 us                                                                     | 358 us: 1.73x slower                                                       |
| coroutines                 | 14.1 ms                                                                    | 24.7 ms: 1.75x slower                                                      |
| go                         | 74.9 ms                                                                    | 131 ms: 1.75x slower                                                       |
| scimark_monte_carlo        | 40.6 ms                                                                    | 71.9 ms: 1.77x slower                                                      |
| spectral_norm              | 62.1 ms                                                                    | 111 ms: 1.79x slower                                                       |
| comprehensions             | 10.8 us                                                                    | 19.3 us: 1.79x slower                                                      |
| hexiom                     | 4.02 ms                                                                    | 7.36 ms: 1.83x slower                                                      |
| mako                       | 6.73 ms                                                                    | 12.4 ms: 1.84x slower                                                      |
| generators                 | 19.8 ms                                                                    | 36.6 ms: 1.85x slower                                                      |
| richards_super             | 30.5 ms                                                                    | 57.0 ms: 1.87x slower                                                      |
| deepcopy_memo              | 17.6 us                                                                    | 33.0 us: 1.87x slower                                                      |
| richards                   | 26.8 ms                                                                    | 50.5 ms: 1.88x slower                                                      |
| deltablue                  | 2.17 ms                                                                    | 4.29 ms: 1.97x slower                                                      |
| scimark_lu                 | 58.0 ms                                                                    | 119 ms: 2.05x slower                                                       |
| unpickle_pure_python       | 133 us                                                                     | 275 us: 2.06x slower                                                       |
| Geometric mean             | (ref)                                                                      | 1.44x slower                                                               |

Benchmark hidden because not significant (2): shortest_path, pidigits
Ignored benchmarks (10) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.305x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.38x
- 95% likely to have a slowdown of 1.38x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: unknown