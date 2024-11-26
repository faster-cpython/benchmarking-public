# Results vs. 3.10.4

- fork: python
- ref: dbd23790dbd662169905
- machine: windows-amd64
- commit hash: dbd2379
- commit date: 2024-11-23
- overall geometric mean: 1.168x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 213 ms: 2.04x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 582 ms: 1.90x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 277 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 397 ms: 1.61x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 80.0 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.1 ms: 1.18x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.63 ms: 1.38x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.20x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 229 us: 1.18x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 41.4 ms: 1.07x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.7 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.6 ms: 1.02x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.4 ms: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.6 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.00 ms: 1.29x faster                                                       |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                        |
| async_tree_none          | 435 ms                                                      | 213 ms: 2.04x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 582 ms: 1.90x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 277 ms: 1.90x faster                                                        |
| pylint                   | 350 ms                                                      | 189 ms: 1.85x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 397 ms: 1.61x faster                                                        |
| go                       | 139 ms                                                      | 89.7 ms: 1.55x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 64.0 ns: 1.48x faster                                                       |
| generators               | 32.4 ms                                                     | 22.4 ms: 1.45x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.4 ms: 1.40x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.63 ms: 1.38x faster                                                       |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                        |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                       |
| raytrace                 | 273 ms                                                      | 202 ms: 1.35x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 63.9 ms: 1.34x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.5 us: 1.34x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 921 us: 1.32x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.30x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.00 ms: 1.29x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.8 ms: 1.28x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.49 ms: 1.28x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.4 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 732 ms: 1.27x faster                                                        |
| pyflate                  | 409 ms                                                      | 324 ms: 1.26x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.5 ms: 1.21x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.20x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.48 sec: 1.20x faster                                                      |
| sympy_sum                | 107 ms                                                      | 89.4 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.5 ms: 1.19x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 807 us: 1.19x faster                                                        |
| scimark_sor              | 106 ms                                                      | 89.7 ms: 1.18x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 229 us: 1.18x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| regex_compile            | 106 ms                                                      | 90.1 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| thrift                   | 617 us                                                      | 535 us: 1.15x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 67.9 ms: 1.14x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.9 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                        |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| float                    | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.5 ms: 1.09x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 41.4 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 555 ms: 1.07x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.5 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.03x faster                                                        |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 94.7 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.71 ms: 1.01x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 76.1 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.34 us: 1.02x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.6 ms: 1.02x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 78.2 ms: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 58.4 ms: 1.05x slower                                                       |
| scimark_fft              | 187 ms                                                      | 201 ms: 1.07x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 247 ms: 1.12x slower                                                        |
| nbody                    | 71.3 ms                                                     | 80.0 ms: 1.12x slower                                                       |
| fannkuch                 | 256 ms                                                      | 289 ms: 1.13x slower                                                        |
| python_startup           | 20.6 ms                                                     | 23.6 ms: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.6 ms: 1.19x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.75 ms: 1.20x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 81.9 ms: 1.32x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.87 ms: 1.32x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (1): logging_format
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241123-3.14.0a2+-dbd2379/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.168x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown