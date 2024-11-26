# Results vs. 3.10.4

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-amd64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.209x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.92 sec                                                    | 1.89 sec: 1.02x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| tornado_http   | 108 ms                                                      | 97.1 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 209 ms: 2.08x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 555 ms: 2.00x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                       |
| nbody          | 71.3 ms                                                     | 54.0 ms: 1.32x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| regex_compile  | 106 ms                                                      | 90.8 ms: 1.17x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.12 ms: 1.50x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 206 us: 1.31x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.26x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.97 ms: 1.82x faster                                                       |
| django_template | 28.9 ms                                                     | 26.9 ms: 1.07x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.9 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 117 us: 2.88x faster                                                        |
| async_tree_none          | 435 ms                                                      | 209 ms: 2.08x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 555 ms: 2.00x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                        |
| mako                     | 9.03 ms                                                     | 4.97 ms: 1.82x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.2 us: 1.78x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.8 ns: 1.70x faster                                                       |
| scimark_sor              | 106 ms                                                      | 63.5 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 53.4 ms: 1.61x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.9 ms: 1.55x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.7 ms: 1.54x faster                                                       |
| go                       | 139 ms                                                      | 91.9 ms: 1.51x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.12 ms: 1.50x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 52.8 ms: 1.46x faster                                                       |
| pylint                   | 350 ms                                                      | 244 ms: 1.44x faster                                                        |
| generators               | 32.4 ms                                                     | 22.7 ms: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                       |
| pyflate                  | 409 ms                                                      | 298 ms: 1.37x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 893 us: 1.36x faster                                                        |
| richards_super           | 52.2 ms                                                     | 38.7 ms: 1.35x faster                                                       |
| deepcopy                 | 255 us                                                      | 190 us: 1.35x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 915 ms: 1.33x faster                                                        |
| float                    | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| nbody                    | 71.3 ms                                                     | 54.0 ms: 1.32x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 453 ms: 1.31x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 206 us: 1.31x faster                                                        |
| pycparser                | 930 ms                                                      | 722 ms: 1.29x faster                                                        |
| raytrace                 | 273 ms                                                      | 216 ms: 1.27x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.26x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 39.9 ms: 1.26x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.18 ms: 1.25x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.20 ms: 1.24x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.6 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.22x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.52 sec: 1.17x faster                                                      |
| regex_compile            | 106 ms                                                      | 90.8 ms: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 828 us: 1.16x faster                                                        |
| thrift                   | 617 us                                                      | 542 us: 1.14x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 5.14 ms: 1.12x faster                                                       |
| tornado_http             | 108 ms                                                      | 97.1 ms: 1.12x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| sympy_sum                | 107 ms                                                      | 102 ms: 1.05x faster                                                        |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.7 ms: 1.04x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                       |
| fannkuch                 | 256 ms                                                      | 247 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.56 us: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 65.5 ms: 1.02x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.89 sec: 1.02x faster                                                      |
| sympy_str                | 194 ms                                                      | 192 ms: 1.01x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.16 us: 1.01x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 15.6 ms: 1.02x slower                                                       |
| sqlglot_normalize        | 205 ms                                                      | 210 ms: 1.02x slower                                                        |
| sympy_expand             | 314 ms                                                      | 323 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 78.5 ms: 1.04x slower                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 42.7 ms: 1.07x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.40 ms: 1.12x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.9 ms: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.1 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.4 ms: 1.19x slower                                                       |
| async_generators         | 222 ms                                                      | 268 ms: 1.21x slower                                                        |
| gc_traversal             | 1.41 ms                                                     | 1.91 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.5 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.71x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): 2to3
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.209x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown