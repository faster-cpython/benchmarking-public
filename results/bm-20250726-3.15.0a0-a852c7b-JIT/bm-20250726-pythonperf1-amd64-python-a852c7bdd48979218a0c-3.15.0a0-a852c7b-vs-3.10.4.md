# Results vs. 3.10.4

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 394 ms: 2.81x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                       |
| async_tree_none         | 435 ms                                                      | 175 ms: 2.48x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 339 ms: 1.88x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                      |
| nbody          | 71.3 ms                                                     | 56.5 ms: 1.26x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.2 ms: 1.34x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.08x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.73x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.12 sec: 1.50x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.42 ms: 1.43x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.32x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.3 ms: 1.08x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.67 us: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.8 ms: 1.02x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| pickle               | 6.85 us                                                     | 7.93 us: 1.16x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.8 us: 1.21x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.43 us: 1.25x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.42 ms: 1.67x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 394 ms: 2.81x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                       |
| async_tree_none          | 435 ms                                                      | 175 ms: 2.48x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 33.4 ms: 2.26x faster                                                      |
| mdp                      | 1.78 sec                                                    | 820 ms: 2.17x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 339 ms: 1.88x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| go                       | 139 ms                                                      | 75.1 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 202 ms: 1.73x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.73x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.1 ns: 1.69x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.42 ms: 1.67x faster                                                      |
| pyflate                  | 409 ms                                                      | 249 ms: 1.64x faster                                                       |
| generators               | 32.4 ms                                                     | 20.2 ms: 1.60x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.57x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 178 ms: 1.54x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.5 ms: 1.52x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| tomli_loads              | 1.67 sec                                                    | 1.12 sec: 1.50x faster                                                     |
| deepcopy                 | 255 us                                                      | 173 us: 1.47x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 497 ms: 1.47x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.4 ms: 1.47x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.42 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.05 ms: 1.42x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.41x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.3 ms: 1.41x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 45.9 ms: 1.36x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 896 ms: 1.36x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.2 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 696 ms: 1.34x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 443 ms: 1.34x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.32x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| nbody                    | 71.3 ms                                                     | 56.5 ms: 1.26x faster                                                      |
| fannkuch                 | 256 ms                                                      | 207 ms: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.6 ms: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 64.3 ms: 1.20x faster                                                      |
| scimark_fft              | 187 ms                                                      | 156 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.2 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.31 ms: 1.18x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.17x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 34.2 ns: 1.16x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 857 us: 1.12x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.3 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.7 ms: 1.08x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.08x faster                                                      |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.67 us: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 72.9 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.8 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.89 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.53 us: 1.05x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.27 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.93 us: 1.16x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 20.8 us: 1.21x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.43 us: 1.25x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.1 ms: 1.31x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 95.8 ms: 1.54x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.18 ms: 1.55x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (2): json, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.302x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown