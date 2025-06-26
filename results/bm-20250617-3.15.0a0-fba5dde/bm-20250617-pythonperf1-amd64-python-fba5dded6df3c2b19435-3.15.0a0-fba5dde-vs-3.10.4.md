# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: windows-amd64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.296x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 395 ms: 2.80x faster                                                       |
| async_tree_none         | 435 ms                                                      | 167 ms: 2.61x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.46x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                      |
| nbody          | 71.3 ms                                                     | 60.5 ms: 1.18x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.7 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 131 us: 1.40x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 206 us: 1.31x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.5 ms: 1.16x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.3 ms: 1.10x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.57 ms: 1.37x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| django_template | 28.9 ms                                                     | 23.6 ms: 1.23x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.33x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 395 ms: 2.80x faster                                                       |
| async_tree_none          | 435 ms                                                      | 167 ms: 2.61x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                      |
| mdp                      | 1.78 sec                                                    | 794 ms: 2.24x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.95x faster                                                       |
| go                       | 139 ms                                                      | 74.0 ms: 1.88x faster                                                      |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.2 ms: 1.73x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.6 ms: 1.59x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 57.7 ms: 1.49x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.91 ms: 1.47x faster                                                      |
| pyflate                  | 409 ms                                                      | 281 ms: 1.45x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.0 ms: 1.43x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.3 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 131 us: 1.40x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.57 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.7 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.7 ms: 1.34x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 699 ms: 1.33x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 206 us: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 59.7 ms: 1.29x faster                                                      |
| thrift                   | 617 us                                                      | 493 us: 1.25x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                     |
| django_template          | 28.9 ms                                                     | 23.6 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.2 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.6 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| nbody                    | 71.3 ms                                                     | 60.5 ms: 1.18x faster                                                      |
| sympy_str                | 194 ms                                                      | 168 ms: 1.16x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.5 ms: 1.16x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                     |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 530 ms: 1.12x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.5 ms: 1.10x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.48 ms: 1.10x faster                                                      |
| sympy_expand             | 314 ms                                                      | 287 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.3 ms: 1.10x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| scimark_fft              | 187 ms                                                      | 173 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                      |
| fannkuch                 | 256 ms                                                      | 247 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.52 ms: 1.15x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.6 ms: 1.30x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.16 ms: 1.53x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 318 ns: 3.36x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, logging_format, xml_etree_generate
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-pythonperf1-amd64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.296x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown