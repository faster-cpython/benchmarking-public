# Results vs. 3.10.4

- fork: python
- ref: b367e27af9b52528e395
- machine: windows-amd64
- commit hash: b367e27
- commit date: 2025-05-30
- overall geometric mean: 1.166x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.80x faster                                                       |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 62.4 ms: 1.14x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.7 ms: 1.33x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.11 ms: 1.50x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.38x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 54.8 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.55 ms: 1.38x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.3 ms: 1.23x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.80x faster                                                       |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.6 ms: 2.39x faster                                                      |
| mdp                      | 1.78 sec                                                    | 795 ms: 2.24x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| go                       | 139 ms                                                      | 75.1 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.68x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.7 us: 1.63x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 56.6 ms: 1.52x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.11 ms: 1.50x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.7 ms: 1.48x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.99 ms: 1.44x faster                                                      |
| pyflate                  | 409 ms                                                      | 286 ms: 1.43x faster                                                       |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| scimark_sor              | 106 ms                                                      | 76.1 ms: 1.40x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.55 ms: 1.38x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.38x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.7 ms: 1.34x faster                                                      |
| regex_compile            | 106 ms                                                      | 79.7 ms: 1.33x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.1 ms: 1.33x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 705 ms: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 33.3 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.1 ms: 1.23x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                      |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                                       |
| nbody                    | 71.3 ms                                                     | 62.4 ms: 1.14x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 854 us: 1.12x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                     |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 530 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.46 ms: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                      |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.2 ms: 1.09x faster                                                      |
| scimark_fft              | 187 ms                                                      | 173 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 70.5 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 54.8 ms: 1.01x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                       |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.50x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 94.4 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 321 ns: 3.39x slower                                                       |
| coverage                 | 39.0 ms                                                     | 290 ms: 7.42x slower                                                       |
| thrift                   | 617 us                                                      | 93.6 ms: 151.65x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): logging_simple
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250530-3.15.0a0-b367e27/bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown