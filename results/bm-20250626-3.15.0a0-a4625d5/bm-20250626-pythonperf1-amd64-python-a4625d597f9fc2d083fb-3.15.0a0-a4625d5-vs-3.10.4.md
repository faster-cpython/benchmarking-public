# Results vs. 3.10.4

- fork: python
- ref: a4625d597f9fc2d083fb
- machine: windows-amd64
- commit hash: a4625d5
- commit date: 2025-06-26
- overall geometric mean: 1.275x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 401 ms: 2.77x faster                                                       |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 210 ms: 2.51x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 333 ms: 1.91x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.4 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.6 ms: 1.32x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.35 ms: 1.44x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.26x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.72 ms: 1.34x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                      |
| django_template | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.29x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 401 ms: 2.77x faster                                                       |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.52x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 210 ms: 2.51x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                      |
| mdp                      | 1.78 sec                                                    | 800 ms: 2.22x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 333 ms: 1.91x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 77.6 ms: 1.79x faster                                                      |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                       |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.68x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.2 ms: 1.68x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.6 ns: 1.64x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.56x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.55x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.35 ms: 1.44x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 60.0 ms: 1.43x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.08 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.8 ms: 1.40x faster                                                      |
| float                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                      |
| pyflate                  | 409 ms                                                      | 292 ms: 1.40x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                       |
| scimark_sor              | 106 ms                                                      | 78.7 ms: 1.35x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.72 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 698 ms: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                      |
| regex_compile            | 106 ms                                                      | 80.6 ms: 1.32x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.6 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.26x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                      |
| thrift                   | 617 us                                                      | 499 us: 1.24x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.3 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.2 ms: 1.23x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.22x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 492 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 64.9 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.7 ms: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| django_template          | 28.9 ms                                                     | 24.5 ms: 1.18x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                     |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                      |
| nbody                    | 71.3 ms                                                     | 65.4 ms: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.6 ms: 1.08x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                                      |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.9 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.04x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.56 us: 1.03x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.13 us: 1.02x faster                                                      |
| scimark_fft              | 187 ms                                                      | 190 ms: 1.01x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                      |
| fannkuch                 | 256 ms                                                      | 261 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| async_generators         | 222 ms                                                      | 236 ms: 1.07x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.60 ms: 1.17x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.6 ms: 1.32x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.49x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250626-3.15.0a0-a4625d5/bm-20250626-pythonperf1-amd64-python-a4625d597f9fc2d083fb-3.15.0a0-a4625d5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.275x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown