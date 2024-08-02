# Results vs. 3.10.4

- fork: python
- ref: d66b06107b0104af513f
- machine: windows-amd64
- commit hash: d66b061
- commit date: 2024-07-19
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                      |
| tornado_http   | 108 ms                                                      | 91.2 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 210 ms: 2.08x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 256 ms: 2.05x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 552 ms: 2.01x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.94x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.4 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 78.2 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.8 ms: 1.24x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.05x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.90 ms: 1.55x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 199 us: 1.36x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 139 us: 1.32x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 39.5 ms: 1.13x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.50 sec: 1.12x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.4 ms: 1.04x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.08 ms: 1.28x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                      |
| django_template | 28.9 ms                                                     | 23.2 ms: 1.25x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.8 ms: 1.22x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.19x faster                                                       |
| async_tree_none          | 435 ms                                                      | 210 ms: 2.08x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 256 ms: 2.05x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.04 ms: 2.05x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 552 ms: 2.01x faster                                                       |
| pylint                   | 350 ms                                                      | 210 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.66x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.4 ns: 1.62x faster                                                      |
| richards_super           | 52.2 ms                                                     | 32.7 ms: 1.60x faster                                                      |
| raytrace                 | 273 ms                                                      | 172 ms: 1.59x faster                                                       |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.56x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.90 ms: 1.55x faster                                                      |
| go                       | 139 ms                                                      | 91.0 ms: 1.53x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.48x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.6 ms: 1.48x faster                                                      |
| deepcopy                 | 255 us                                                      | 174 us: 1.47x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.6 us: 1.47x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.6 ms: 1.47x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 854 us: 1.42x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.40x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.14 ms: 1.39x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 534 ms: 1.37x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 199 us: 1.36x faster                                                       |
| pyflate                  | 409 ms                                                      | 302 ms: 1.35x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.59 sec: 1.33x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 139 us: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.6 ms: 1.29x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.08 ms: 1.28x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                      |
| scimark_sor              | 106 ms                                                      | 84.4 ms: 1.26x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.8 ms: 1.25x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.2 ms: 1.25x faster                                                      |
| regex_compile            | 106 ms                                                      | 85.8 ms: 1.24x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.4 ms: 1.23x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 33.8 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.7 ms: 1.21x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.21x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 800 us: 1.20x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                                      |
| tornado_http             | 108 ms                                                      | 91.2 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.6 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 181 ms: 1.13x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 523 ms: 1.13x faster                                                       |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.5 ms: 1.13x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 68.9 ms: 1.12x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.50 sec: 1.12x faster                                                     |
| float                    | 61.7 ms                                                     | 55.4 ms: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.7 ms: 1.10x faster                                                      |
| pycparser                | 930 ms                                                      | 848 ms: 1.10x faster                                                       |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 294 ms: 1.07x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.46 us: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.98 us: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.0 ms: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.8 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.4 ms: 1.04x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.3 ms: 1.06x slower                                                      |
| scimark_fft              | 187 ms                                                      | 199 ms: 1.06x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 67.1 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                       |
| fannkuch                 | 256 ms                                                      | 280 ms: 1.10x slower                                                       |
| nbody                    | 71.3 ms                                                     | 78.2 ms: 1.10x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 903 us: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.3 ms: 1.21x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.82 ms: 1.22x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                               |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240719-3.14.0a0-d66b061/bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown