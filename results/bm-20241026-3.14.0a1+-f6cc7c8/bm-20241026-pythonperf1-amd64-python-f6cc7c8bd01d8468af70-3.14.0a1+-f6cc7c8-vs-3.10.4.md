# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-amd64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.159x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 42.0 ms: 1.21x faster                                                       |
| tornado_http   | 108 ms                                                      | 93.0 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 218 ms: 2.00x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 564 ms: 1.96x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 278 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.9 ms: 1.12x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 78.1 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_compile  | 106 ms                                                      | 91.6 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.84 ms: 1.34x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 223 us: 1.21x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.60 sec: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.7 ms: 1.03x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.8 ms: 1.04x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.5 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.82 ms: 1.33x faster                                                       |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                        |
| async_tree_none          | 435 ms                                                      | 218 ms: 2.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 564 ms: 1.96x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 278 ms: 1.89x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                        |
| go                       | 139 ms                                                      | 88.0 ms: 1.58x faster                                                       |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 62.2 ns: 1.52x faster                                                       |
| generators               | 32.4 ms                                                     | 21.7 ms: 1.49x faster                                                       |
| richards_super           | 52.2 ms                                                     | 35.8 ms: 1.46x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.1 us: 1.43x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 61.2 ms: 1.40x faster                                                       |
| raytrace                 | 273 ms                                                      | 196 ms: 1.39x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.84 ms: 1.34x faster                                                       |
| deepcopy                 | 255 us                                                      | 193 us: 1.33x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.82 ms: 1.33x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.5 us: 1.32x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 922 us: 1.32x faster                                                        |
| richards                 | 42.4 ms                                                     | 32.2 ms: 1.32x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.40 ms: 1.31x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.29x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.1 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 734 ms: 1.27x faster                                                        |
| pyflate                  | 409 ms                                                      | 323 ms: 1.27x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.1 ms: 1.22x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.0 ms: 1.21x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 223 us: 1.21x faster                                                        |
| sympy_sum                | 107 ms                                                      | 89.7 ms: 1.19x faster                                                       |
| scimark_sor              | 106 ms                                                      | 90.6 ms: 1.17x faster                                                       |
| tornado_http             | 108 ms                                                      | 93.0 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_compile            | 106 ms                                                      | 91.6 ms: 1.16x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.7 ms: 1.15x faster                                                       |
| thrift                   | 617 us                                                      | 538 us: 1.15x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.56 sec: 1.14x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 68.3 ms: 1.13x faster                                                       |
| float                    | 61.7 ms                                                     | 54.9 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 852 us: 1.12x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.2 ms: 1.05x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 562 ms: 1.05x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.60 sec: 1.05x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                        |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                        |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 76.8 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.7 ms: 1.03x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.95 us: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.8 ms: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.51 us: 1.05x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 80.5 ms: 1.06x slower                                                       |
| async_generators         | 222 ms                                                      | 242 ms: 1.09x slower                                                        |
| nbody                    | 71.3 ms                                                     | 78.1 ms: 1.09x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.5 us: 1.11x slower                                                       |
| fannkuch                 | 256 ms                                                      | 283 ms: 1.11x slower                                                        |
| scimark_fft              | 187 ms                                                      | 209 ms: 1.12x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.87 ms: 1.24x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 84.6 ms: 1.36x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.93 ms: 1.37x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.40 ms: 1.75x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_parse, scimark_sparse_mat_mult, json, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1-amd64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.159x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown