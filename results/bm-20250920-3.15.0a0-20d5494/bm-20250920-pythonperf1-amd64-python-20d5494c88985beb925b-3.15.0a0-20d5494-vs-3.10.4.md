# Results vs. 3.10.4

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.286x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 444 ms: 2.49x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 233 ms: 2.26x faster                                                       |
| async_tree_none         | 435 ms                                                      | 199 ms: 2.19x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 350 ms: 1.82x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.18x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 63.7 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.7 ms: 1.33x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.42 ms: 1.69x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.0 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 86.8 ms: 1.12x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.38 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 55.2 ms: 1.01x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.99 us: 1.10x slower                                                      |
| pickle               | 6.85 us                                                     | 7.87 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.7 us: 1.21x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.40 us: 1.24x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.7 ms: 1.21x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.70 ms: 1.35x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                      |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.5 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.24x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.9 ms: 2.53x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 444 ms: 2.49x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 233 ms: 2.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 792 ms: 2.25x faster                                                       |
| async_tree_none          | 435 ms                                                      | 199 ms: 2.19x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 350 ms: 1.82x faster                                                       |
| go                       | 139 ms                                                      | 76.6 ms: 1.81x faster                                                      |
| pylint                   | 350 ms                                                      | 193 ms: 1.81x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.2 ns: 1.71x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.42 ms: 1.69x faster                                                      |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 17.7 us: 1.62x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.2 ms: 1.56x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.38 sec: 1.53x faster                                                     |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 57.8 ms: 1.48x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.48x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 501 ms: 1.46x faster                                                       |
| raytrace                 | 273 ms                                                      | 188 ms: 1.46x faster                                                       |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.8 ms: 1.44x faster                                                      |
| scimark_sor              | 106 ms                                                      | 74.2 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.21 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.70 ms: 1.35x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.7 ms: 1.33x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 38.4 ms: 1.31x faster                                                      |
| pycparser                | 930 ms                                                      | 711 ms: 1.31x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                       |
| sympy_sum                | 107 ms                                                      | 84.4 ms: 1.27x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.2 ms: 1.25x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 993 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                      |
| thrift                   | 617 us                                                      | 504 us: 1.22x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 487 ms: 1.21x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 65.3 ms: 1.18x faster                                                      |
| sympy_str                | 194 ms                                                      | 166 ms: 1.18x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.5 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.0 ms: 1.14x faster                                                      |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                      |
| sympy_expand             | 314 ms                                                      | 281 ms: 1.12x faster                                                       |
| nbody                    | 71.3 ms                                                     | 63.7 ms: 1.12x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 86.8 ms: 1.12x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 860 us: 1.11x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.38 us: 1.08x faster                                                      |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.08x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.9 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.54 ms: 1.07x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.3 ms: 1.07x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.42 us: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 38.0 ns: 1.04x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.97 us: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.6 ms: 1.03x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 55.2 ms: 1.01x faster                                                      |
| fannkuch                 | 256 ms                                                      | 263 ms: 1.03x slower                                                       |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.99 us: 1.10x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.87 us: 1.15x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.7 us: 1.21x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.7 ms: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.40 us: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 90.0 ms: 1.45x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.05 ms: 1.45x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (3): pidigits, json_loads, scimark_fft
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.286x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown