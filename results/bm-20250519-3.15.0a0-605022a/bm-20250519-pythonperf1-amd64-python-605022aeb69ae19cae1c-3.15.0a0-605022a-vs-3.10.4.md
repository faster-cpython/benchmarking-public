# Results vs. 3.10.4

- fork: python
- ref: 605022aeb69ae19cae1c
- machine: windows-amd64
- commit hash: 605022a
- commit date: 2025-05-19
- overall geometric mean: 1.175x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 395 ms: 2.81x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.57x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.5 ms: 1.45x faster                                                      |
| nbody          | 71.3 ms                                                     | 61.6 ms: 1.16x faster                                                      |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.9 ms: 1.33x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.17 ms: 1.48x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.34x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.29x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.0 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.47 ms: 1.40x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                      |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.12x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 395 ms: 2.81x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.57x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.6 ms: 2.56x faster                                                      |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| mdp                      | 1.78 sec                                                    | 779 ms: 2.29x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.12 ms: 1.98x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| go                       | 139 ms                                                      | 78.1 ms: 1.78x faster                                                      |
| pylint                   | 350 ms                                                      | 197 ms: 1.77x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.63x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.1 ms: 1.62x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                      |
| raytrace                 | 273 ms                                                      | 178 ms: 1.54x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.2 us: 1.50x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 57.8 ms: 1.49x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.17 ms: 1.48x faster                                                      |
| deepcopy                 | 255 us                                                      | 173 us: 1.47x faster                                                       |
| pyflate                  | 409 ms                                                      | 280 ms: 1.46x faster                                                       |
| float                    | 61.7 ms                                                     | 42.5 ms: 1.45x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.99 ms: 1.44x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.4 ms: 1.42x faster                                                      |
| scimark_sor              | 106 ms                                                      | 76.0 ms: 1.40x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.47 ms: 1.40x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.34x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.5 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                      |
| regex_compile            | 106 ms                                                      | 79.9 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.29x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 994 ms: 1.23x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| sympy_sum                | 107 ms                                                      | 87.7 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 489 ms: 1.21x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                      |
| nbody                    | 71.3 ms                                                     | 61.6 ms: 1.16x faster                                                      |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 840 us: 1.14x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                      |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.46 ms: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.6 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                      |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                       |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                      |
| fannkuch                 | 256 ms                                                      | 246 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.0 ms: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.91 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 229 ms: 1.03x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.44 us: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.0 us: 1.07x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.0 ms: 1.21x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.48x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 92.0 ms: 1.48x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.28 ms: 1.60x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 316 ns: 3.33x slower                                                       |
| coverage                 | 39.0 ms                                                     | 295 ms: 7.56x slower                                                       |
| thrift                   | 617 us                                                      | 92.4 ms: 149.72x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                               |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250519-3.15.0a0-605022a/bm-20250519-pythonperf1-amd64-python-605022aeb69ae19cae1c-3.15.0a0-605022a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.175x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown