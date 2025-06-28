# Results vs. 3.10.4

- fork: python
- ref: c419af9e277bea7dd78f
- machine: windows-amd64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.303x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.52x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                      |
| nbody          | 71.3 ms                                                     | 53.5 ms: 1.33x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.8 ms: 1.33x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.69x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.14 sec: 1.46x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 34.6 ms: 1.28x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.54 ms: 1.63x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                      |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.18x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.52x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.6 ms: 2.40x faster                                                      |
| mdp                      | 1.78 sec                                                    | 806 ms: 2.21x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.84x faster                                                      |
| go                       | 139 ms                                                      | 79.3 ms: 1.75x faster                                                      |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.8 ns: 1.73x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.69x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.2 ms: 1.67x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.54 ms: 1.63x faster                                                      |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.1 us: 1.59x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.7 ms: 1.53x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.2 ms: 1.50x faster                                                      |
| deepcopy                 | 255 us                                                      | 173 us: 1.47x faster                                                       |
| raytrace                 | 273 ms                                                      | 186 ms: 1.47x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.14 sec: 1.46x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| float                    | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.5 ms: 1.38x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 62.4 ms: 1.38x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.25 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.5 ms: 1.35x faster                                                      |
| nbody                    | 71.3 ms                                                     | 53.5 ms: 1.33x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 915 ms: 1.33x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.8 ms: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 701 ms: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 453 ms: 1.31x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 34.6 ms: 1.28x faster                                                      |
| scimark_sor              | 106 ms                                                      | 83.0 ms: 1.28x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.24x faster                                                      |
| thrift                   | 617 us                                                      | 500 us: 1.24x faster                                                       |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.23x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.7 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 64.2 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.27 ms: 1.20x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| fannkuch                 | 256 ms                                                      | 224 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.10x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                                      |
| coroutines               | 16.0 ms                                                     | 15.0 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.2 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.56 us: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.19 us: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.25 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 242 ms: 1.09x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.0 ms: 1.31x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.52x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.31x faster                                                               |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.303x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown