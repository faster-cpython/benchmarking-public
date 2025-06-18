# Results vs. 3.10.4

- fork: python
- ref: 8dd8b5c2f0785675b928
- machine: windows-amd64
- commit hash: 8dd8b5c
- commit date: 2025-06-17
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.52x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                      |
| nbody          | 71.3 ms                                                     | 61.8 ms: 1.15x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.9 ms: 1.34x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.37x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.34x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.52x faster                                                       |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                      |
| mdp                      | 1.78 sec                                                    | 800 ms: 2.23x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                      |
| go                       | 139 ms                                                      | 74.9 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.6 us: 1.63x faster                                                      |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.63x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                      |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.0 ms: 1.48x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.02 ms: 1.43x faster                                                      |
| pyflate                  | 409 ms                                                      | 289 ms: 1.42x faster                                                       |
| scimark_sor              | 106 ms                                                      | 75.0 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.6 ms: 1.41x faster                                                      |
| float                    | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.37x faster                                                       |
| regex_compile            | 106 ms                                                      | 78.9 ms: 1.34x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.1 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 710 ms: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.1 ms: 1.24x faster                                                      |
| thrift                   | 617 us                                                      | 500 us: 1.24x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.2 ms: 1.23x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| sympy_str                | 194 ms                                                      | 168 ms: 1.16x faster                                                       |
| nbody                    | 71.3 ms                                                     | 61.8 ms: 1.15x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                     |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 537 ms: 1.10x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                      |
| sympy_expand             | 314 ms                                                      | 286 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.9 ms: 1.09x faster                                                      |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.52 ms: 1.08x faster                                                      |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.5 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| fannkuch                 | 256 ms                                                      | 257 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.28 us: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                                      |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.55 ms: 1.16x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.0 ms: 1.26x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.68x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 342 ns: 3.62x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, logging_format
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-8dd8b5c/bm-20250617-pythonperf1-amd64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.283x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown