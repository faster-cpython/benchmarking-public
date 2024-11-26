# Results vs. 3.10.4

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-amd64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                       |
| tornado_http   | 108 ms                                                      | 93.4 ms: 1.16x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 566 ms: 1.96x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 278 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 382 ms: 1.67x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.9 ms: 1.12x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 79.4 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| regex_compile  | 106 ms                                                      | 92.2 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 159 us: 1.15x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 95.5 ms: 1.01x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.6 ms: 1.04x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.8 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.95 ms: 1.30x faster                                                       |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.6 ms: 1.12x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.04x faster                                                        |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 566 ms: 1.96x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 278 ms: 1.89x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 382 ms: 1.67x faster                                                        |
| pylint                   | 350 ms                                                      | 224 ms: 1.56x faster                                                        |
| go                       | 139 ms                                                      | 90.1 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 65.6 ns: 1.44x faster                                                       |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                       |
| raytrace                 | 273 ms                                                      | 199 ms: 1.37x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.73 ms: 1.36x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                       |
| richards_super           | 52.2 ms                                                     | 38.5 ms: 1.36x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.5 us: 1.34x faster                                                       |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 64.5 ms: 1.33x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.95 ms: 1.30x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 938 us: 1.30x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 48.6 ms: 1.29x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.16 ms: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 734 ms: 1.27x faster                                                        |
| pyflate                  | 409 ms                                                      | 324 ms: 1.26x faster                                                        |
| richards                 | 42.4 ms                                                     | 34.0 ms: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.60 ms: 1.25x faster                                                       |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| sympy_sum                | 107 ms                                                      | 90.2 ms: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.51 sec: 1.18x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.0 ms: 1.17x faster                                                       |
| thrift                   | 617 us                                                      | 531 us: 1.16x faster                                                        |
| tornado_http             | 108 ms                                                      | 93.4 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 826 us: 1.16x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 159 us: 1.15x faster                                                        |
| regex_compile            | 106 ms                                                      | 92.2 ms: 1.15x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.9 ms: 1.15x faster                                                       |
| scimark_sor              | 106 ms                                                      | 93.0 ms: 1.14x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.6 ms: 1.12x faster                                                       |
| float                    | 61.7 ms                                                     | 54.9 ms: 1.12x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 71.6 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 551 ms: 1.07x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 37.3 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.3 ms: 1.04x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 198 ms: 1.04x faster                                                        |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 95.5 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.97 us: 1.03x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.6 ms: 1.04x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 78.9 ms: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.50 us: 1.04x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                       |
| async_generators         | 222 ms                                                      | 243 ms: 1.09x slower                                                        |
| scimark_fft              | 187 ms                                                      | 206 ms: 1.10x slower                                                        |
| nbody                    | 71.3 ms                                                     | 79.4 ms: 1.11x slower                                                       |
| fannkuch                 | 256 ms                                                      | 289 ms: 1.13x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.8 ms: 1.16x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.7 ms: 1.20x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.84 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 83.1 ms: 1.34x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.91 ms: 1.35x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.36 ms: 1.71x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                                |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.158x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown