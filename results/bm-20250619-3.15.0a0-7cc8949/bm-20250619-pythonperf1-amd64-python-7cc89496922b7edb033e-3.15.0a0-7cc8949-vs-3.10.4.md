# Results vs. 3.10.4

- fork: python
- ref: 7cc89496922b7edb033e
- machine: windows-amd64
- commit hash: 7cc8949
- commit date: 2025-06-19
- overall geometric mean: 1.266x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 211 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                                      |
| nbody          | 71.3 ms                                                     | 66.3 ms: 1.07x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.2 ms: 1.31x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.25x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.1 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.86 ms: 1.32x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.23x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                       |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 211 ms: 2.50x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.6 ms: 2.39x faster                                                      |
| mdp                      | 1.78 sec                                                    | 814 ms: 2.19x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                      |
| go                       | 139 ms                                                      | 77.4 ms: 1.80x faster                                                      |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.4 ms: 1.55x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.4 ms: 1.49x faster                                                      |
| raytrace                 | 273 ms                                                      | 184 ms: 1.49x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.23 ms: 1.47x faster                                                      |
| deepcopy                 | 255 us                                                      | 174 us: 1.47x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 59.0 ms: 1.46x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.7 ms: 1.44x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                      |
| pyflate                  | 409 ms                                                      | 296 ms: 1.38x faster                                                       |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                                      |
| scimark_sor              | 106 ms                                                      | 78.4 ms: 1.35x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.86 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                       |
| regex_compile            | 106 ms                                                      | 81.2 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 48.3 ms: 1.29x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.4 ms: 1.24x faster                                                      |
| thrift                   | 617 us                                                      | 501 us: 1.23x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.9 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                     |
| tomli_loads              | 1.67 sec                                                    | 1.45 sec: 1.15x faster                                                     |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.08x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                      |
| nbody                    | 71.3 ms                                                     | 66.3 ms: 1.07x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.1 ms: 1.07x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 555 ms: 1.07x faster                                                       |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.5 ms: 1.03x faster                                                      |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.90 us: 1.02x slower                                                      |
| fannkuch                 | 256 ms                                                      | 261 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.1 ms: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.46 us: 1.04x slower                                                      |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.62 ms: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.0 ms: 1.26x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.16 ms: 1.54x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 327 ns: 3.45x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-7cc8949/bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.266x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown