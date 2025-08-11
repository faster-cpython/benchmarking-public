# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.59 sec: 1.21x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.2 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 382 ms: 2.90x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 200 ms: 2.62x faster                                                       |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 327 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.48x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.1 ms: 1.43x faster                                                      |
| nbody          | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.4 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.27 ms: 1.74x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 132 us: 1.39x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.30x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.8 ms: 1.15x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 86.8 ms: 1.12x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.60 us: 1.06x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.5 ms: 1.04x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.81 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.82 us: 1.14x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.6 us: 1.14x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.33 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.53 ms: 1.38x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.29x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 382 ms: 2.90x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 200 ms: 2.62x faster                                                       |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.54x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                      |
| mdp                      | 1.78 sec                                                    | 790 ms: 2.25x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 327 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.20 ms: 1.91x faster                                                      |
| go                       | 139 ms                                                      | 75.6 ms: 1.84x faster                                                      |
| pylint                   | 350 ms                                                      | 193 ms: 1.82x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.27 ms: 1.74x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.1 ms: 1.74x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.0 ns: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.1 ms: 1.62x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.7 ms: 1.55x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 55.9 ms: 1.53x faster                                                      |
| deepcopy                 | 255 us                                                      | 167 us: 1.53x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.9 ms: 1.47x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.97 ms: 1.45x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 509 ms: 1.44x faster                                                       |
| float                    | 61.7 ms                                                     | 43.1 ms: 1.43x faster                                                      |
| pyflate                  | 409 ms                                                      | 289 ms: 1.42x faster                                                       |
| raytrace                 | 273 ms                                                      | 193 ms: 1.42x faster                                                       |
| scimark_sor              | 106 ms                                                      | 75.7 ms: 1.40x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.39x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.53 ms: 1.38x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.2 ms: 1.37x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.4 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 689 ms: 1.35x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.30x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 39.1 ms: 1.29x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| thrift                   | 617 us                                                      | 489 us: 1.26x faster                                                       |
| sympy_sum                | 107 ms                                                      | 85.2 ms: 1.26x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.77 us: 1.25x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 988 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 487 ms: 1.22x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.59 sec: 1.21x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                      |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                       |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 66.0 ms: 1.17x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.8 ms: 1.15x faster                                                      |
| sympy_expand             | 314 ms                                                      | 279 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 86.8 ms: 1.12x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 862 us: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.46 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.8 ms: 1.10x faster                                                      |
| nbody                    | 71.3 ms                                                     | 65.2 ms: 1.09x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 37.1 ns: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.5 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.60 us: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.41 us: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.99 us: 1.04x faster                                                      |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| scimark_fft              | 187 ms                                                      | 182 ms: 1.03x faster                                                       |
| fannkuch                 | 256 ms                                                      | 262 ms: 1.02x slower                                                       |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.5 ms: 1.04x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.81 us: 1.04x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.47 ms: 1.13x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.82 us: 1.14x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.6 us: 1.14x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.33 us: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.5 ms: 1.27x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.49x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 94.9 ms: 1.53x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.30 ms: 1.63x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.302x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown