# Results vs. 3.10.4

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: windows-amd64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.295x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 396 ms: 2.80x faster                                                       |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.58x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 57.7 ms: 1.24x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 114 us: 1.60x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 6.32 ms: 1.45x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.16 sec: 1.44x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 206 us: 1.31x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.2 ms: 1.06x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.22x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.42 ms: 1.67x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 396 ms: 2.80x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.58x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.7 ms: 2.39x faster                                                      |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| go                       | 139 ms                                                      | 78.0 ms: 1.78x faster                                                      |
| pylint                   | 350 ms                                                      | 202 ms: 1.73x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.42 ms: 1.67x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.65x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                      |
| generators               | 32.4 ms                                                     | 20.0 ms: 1.62x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 114 us: 1.60x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                                      |
| pyflate                  | 409 ms                                                      | 264 ms: 1.55x faster                                                       |
| deepcopy                 | 255 us                                                      | 167 us: 1.53x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.1 ms: 1.51x faster                                                      |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.32 ms: 1.45x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.16 sec: 1.44x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 60.5 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| scimark_sor              | 106 ms                                                      | 77.1 ms: 1.38x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.21 ms: 1.37x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.4 ms: 1.35x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 698 ms: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 206 us: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| thrift                   | 617 us                                                      | 491 us: 1.26x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 61.5 ms: 1.26x faster                                                      |
| nbody                    | 71.3 ms                                                     | 57.7 ms: 1.24x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.3 ms: 1.23x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.21x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.30 ms: 1.19x faster                                                      |
| scimark_fft              | 187 ms                                                      | 160 ms: 1.17x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                     |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 520 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.2 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.07x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.2 ms: 1.06x faster                                                      |
| fannkuch                 | 256 ms                                                      | 241 ms: 1.06x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.3 ms: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| json                     | 3.14 ms                                                     | 3.11 ms: 1.01x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| async_generators         | 222 ms                                                      | 242 ms: 1.09x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.36 ms: 1.11x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.5 ms: 1.29x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.68x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 322 ns: 3.40x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, logging_format, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.295x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown