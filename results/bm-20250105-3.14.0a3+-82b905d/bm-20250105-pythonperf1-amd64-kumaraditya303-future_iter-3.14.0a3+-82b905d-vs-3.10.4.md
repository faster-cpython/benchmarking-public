# Results vs. 3.10.4

- fork: kumaraditya303
- ref: future_iter
- machine: windows-amd64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.182x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.4 ms: 1.29x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 405 ms: 2.74x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 219 ms: 2.40x faster                                                       |
| async_tree_none         | 435 ms                                                      | 182 ms: 2.39x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 347 ms: 1.84x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.4 ms: 1.18x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| nbody          | 71.3 ms                                                     | 78.7 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| regex_compile  | 106 ms                                                      | 89.2 ms: 1.19x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 22.8 ms: 1.48x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.68 ms: 1.37x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 226 us: 1.19x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 154 us: 1.19x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.0 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                      |
| python_startup         | 20.6 ms                                                     | 23.0 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.05 ms: 1.28x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                      |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 405 ms: 2.74x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 219 ms: 2.40x faster                                                       |
| async_tree_none          | 435 ms                                                      | 182 ms: 2.39x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 347 ms: 1.84x faster                                                       |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                       |
| go                       | 139 ms                                                      | 90.1 ms: 1.54x faster                                                      |
| generators               | 32.4 ms                                                     | 21.3 ms: 1.52x faster                                                      |
| richards_super           | 52.2 ms                                                     | 35.4 ms: 1.48x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.3 ms: 1.43x faster                                                      |
| raytrace                 | 273 ms                                                      | 192 ms: 1.43x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 66.8 ns: 1.42x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.68 ms: 1.37x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 895 us: 1.36x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.2 us: 1.36x faster                                                      |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                       |
| richards                 | 42.4 ms                                                     | 31.3 ms: 1.35x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.6 us: 1.31x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 66.2 ms: 1.30x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 39.4 ms: 1.29x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.05 ms: 1.28x faster                                                      |
| pycparser                | 930 ms                                                      | 733 ms: 1.27x faster                                                       |
| pyflate                  | 409 ms                                                      | 323 ms: 1.27x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.54 ms: 1.27x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.9 ms: 1.25x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 63.4 ms: 1.22x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                      |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 226 us: 1.19x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.2 ms: 1.19x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 154 us: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.3 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.8 ms: 1.18x faster                                                      |
| float                    | 61.7 ms                                                     | 52.4 ms: 1.18x faster                                                      |
| sympy_sum                | 107 ms                                                      | 91.0 ms: 1.18x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 828 us: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                      |
| scimark_sor              | 106 ms                                                      | 92.5 ms: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                      |
| thrift                   | 617 us                                                      | 546 us: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.2 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                     |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 556 ms: 1.06x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                                      |
| json                     | 3.14 ms                                                     | 3.11 ms: 1.01x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.31 us: 1.01x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.77 ms: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.7 ms: 1.02x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                      |
| json_loads               | 14.0 us                                                     | 15.0 us: 1.07x slower                                                      |
| async_generators         | 222 ms                                                      | 237 ms: 1.07x slower                                                       |
| scimark_fft              | 187 ms                                                      | 203 ms: 1.08x slower                                                       |
| fannkuch                 | 256 ms                                                      | 280 ms: 1.10x slower                                                       |
| nbody                    | 71.3 ms                                                     | 78.7 ms: 1.10x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                      |
| python_startup           | 20.6 ms                                                     | 23.0 ms: 1.12x slower                                                      |
| mypy2                    | 555 ms                                                      | 640 ms: 1.15x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.92 ms: 1.25x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 82.4 ms: 1.33x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.40x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 22.8 ms: 1.48x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (3): nqueens, logging_format, pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.182x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown