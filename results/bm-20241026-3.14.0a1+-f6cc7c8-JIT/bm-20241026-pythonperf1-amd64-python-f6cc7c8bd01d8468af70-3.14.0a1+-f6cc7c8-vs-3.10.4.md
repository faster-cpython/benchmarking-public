# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-amd64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.194x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 250 ms: 1.02x slower                                                        |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.31x faster                                                       |
| tornado_http   | 108 ms                                                      | 98.7 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 539 ms: 2.06x faster                                                        |
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 266 ms: 1.98x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 396 ms: 1.61x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 53.7 ms: 1.33x faster                                                       |
| float          | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.5 ms: 1.16x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.18 ms: 1.48x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 144 us: 1.27x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 95.9 ms: 1.01x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.06 ms: 1.78x faster                                                       |
| django_template | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.3 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.89x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 539 ms: 2.06x faster                                                        |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 266 ms: 1.98x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.06 ms: 1.78x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.8 us: 1.72x faster                                                       |
| scimark_sor              | 106 ms                                                      | 64.9 ms: 1.64x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.4 ns: 1.62x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 396 ms: 1.61x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 40.5 ms: 1.54x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.2 ms: 1.54x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 56.2 ms: 1.53x faster                                                       |
| go                       | 139 ms                                                      | 91.8 ms: 1.51x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.9 ms: 1.51x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.18 ms: 1.48x faster                                                       |
| generators               | 32.4 ms                                                     | 22.9 ms: 1.42x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                       |
| pyflate                  | 409 ms                                                      | 292 ms: 1.40x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 886 us: 1.37x faster                                                        |
| richards_super           | 52.2 ms                                                     | 38.5 ms: 1.36x faster                                                       |
| deepcopy                 | 255 us                                                      | 190 us: 1.35x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 57.6 ms: 1.34x faster                                                       |
| nbody                    | 71.3 ms                                                     | 53.7 ms: 1.33x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                        |
| raytrace                 | 273 ms                                                      | 208 ms: 1.31x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.31x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                      |
| float                    | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 950 ms: 1.28x faster                                                        |
| pycparser                | 930 ms                                                      | 727 ms: 1.28x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 144 us: 1.27x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 468 ms: 1.27x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.18 ms: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                                       |
| pylint                   | 350 ms                                                      | 281 ms: 1.25x faster                                                        |
| richards                 | 42.4 ms                                                     | 34.4 ms: 1.23x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                                       |
| scimark_fft              | 187 ms                                                      | 155 ms: 1.21x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                       |
| thrift                   | 617 us                                                      | 532 us: 1.16x faster                                                        |
| regex_compile            | 106 ms                                                      | 91.5 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 839 us: 1.14x faster                                                        |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                       |
| tornado_http             | 108 ms                                                      | 98.7 ms: 1.10x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.63 sec: 1.10x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 5.26 ms: 1.09x faster                                                       |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.07x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                       |
| fannkuch                 | 256 ms                                                      | 240 ms: 1.07x faster                                                        |
| sympy_sum                | 107 ms                                                      | 103 ms: 1.04x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 64.1 ms: 1.04x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| sympy_str                | 194 ms                                                      | 191 ms: 1.02x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.63 us: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.7 ms: 1.02x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 95.9 ms: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.30 us: 1.01x slower                                                       |
| 2to3                     | 246 ms                                                      | 250 ms: 1.02x slower                                                        |
| sqlglot_normalize        | 205 ms                                                      | 210 ms: 1.02x slower                                                        |
| sympy_integrate          | 15.3 ms                                                     | 15.7 ms: 1.03x slower                                                       |
| sympy_expand             | 314 ms                                                      | 326 ms: 1.04x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 81.2 ms: 1.07x slower                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 42.9 ms: 1.08x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.3 ms: 1.13x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.53 ms: 1.15x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                       |
| async_generators         | 222 ms                                                      | 267 ms: 1.20x slower                                                        |
| coverage                 | 39.0 ms                                                     | 49.0 ms: 1.26x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.95 ms: 1.38x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.3 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.41 ms: 1.76x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (3): docutils, pidigits, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.194x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown