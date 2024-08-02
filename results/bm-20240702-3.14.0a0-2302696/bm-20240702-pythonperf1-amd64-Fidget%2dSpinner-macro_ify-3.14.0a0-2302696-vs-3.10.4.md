# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: macro_ify
- machine: windows-amd64
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                    |
| html5lib       | 51.0 ms                                                     | 36.1 ms: 1.41x faster                                                     |
| tornado_http   | 108 ms                                                      | 80.2 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                       | 1.27x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 201 ms: 2.16x faster                                                      |
| async_tree_memoization  | 526 ms                                                      | 245 ms: 2.15x faster                                                      |
| async_tree_io           | 1.11 sec                                                    | 517 ms: 2.14x faster                                                      |
| async_tree_cpu_io_mixed | 638 ms                                                      | 376 ms: 1.70x faster                                                      |
| Geometric mean          | (ref)                                                       | 2.03x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.5 ms: 1.18x faster                                                     |
| nbody          | 71.3 ms                                                     | 73.2 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                       | 1.05x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.4 ms: 1.34x faster                                                     |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                     |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.14x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 185 us: 1.46x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 131 us: 1.39x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                     |
| tomli_loads          | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                    |
| xml_etree_parse      | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                                     |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.6 ms: 1.04x faster                                                     |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.78 ms: 1.33x faster                                                     |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                     |
| django_template | 28.9 ms                                                     | 22.5 ms: 1.28x faster                                                     |
| genshi_xml      | 41.0 ms                                                     | 32.7 ms: 1.25x faster                                                     |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.32x faster                                                      |
| async_tree_none          | 435 ms                                                      | 201 ms: 2.16x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 245 ms: 2.15x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 517 ms: 2.14x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.02 ms: 2.07x faster                                                     |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                     |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 376 ms: 1.70x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.9 ns: 1.63x faster                                                     |
| raytrace                 | 273 ms                                                      | 168 ms: 1.62x faster                                                      |
| go                       | 139 ms                                                      | 86.0 ms: 1.61x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                     |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                     |
| richards                 | 42.4 ms                                                     | 27.2 ms: 1.56x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 18.4 us: 1.56x faster                                                     |
| chaos                    | 61.7 ms                                                     | 39.6 ms: 1.56x faster                                                     |
| generators               | 32.4 ms                                                     | 21.0 ms: 1.54x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 482 ms: 1.52x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 808 us: 1.50x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 57.0 ms: 1.50x faster                                                     |
| deepcopy                 | 255 us                                                      | 173 us: 1.48x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 185 us: 1.46x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.97 ms: 1.45x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 1.02 ms: 1.44x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 36.1 ms: 1.41x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 131 us: 1.39x faster                                                      |
| pyflate                  | 409 ms                                                      | 295 ms: 1.38x faster                                                      |
| tornado_http             | 108 ms                                                      | 80.2 ms: 1.35x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.57 sec: 1.34x faster                                                    |
| regex_compile            | 106 ms                                                      | 79.4 ms: 1.34x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                     |
| mako                     | 9.03 ms                                                     | 6.78 ms: 1.33x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.3 ms: 1.32x faster                                                     |
| scimark_sor              | 106 ms                                                      | 80.4 ms: 1.32x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                     |
| django_template          | 28.9 ms                                                     | 22.5 ms: 1.28x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 748 us: 1.28x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.76 us: 1.26x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 32.7 ms: 1.25x faster                                                     |
| sympy_sum                | 107 ms                                                      | 85.6 ms: 1.25x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.25x faster                                                    |
| spectral_norm            | 77.3 ms                                                     | 63.2 ms: 1.22x faster                                                     |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                     |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.02 sec: 1.20x faster                                                    |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.20x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 33.4 ms: 1.19x faster                                                     |
| sympy_str                | 194 ms                                                      | 163 ms: 1.19x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 499 ms: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                    |
| float                    | 61.7 ms                                                     | 52.5 ms: 1.18x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 38.1 ms: 1.17x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 178 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                    |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                                      |
| pycparser                | 930 ms                                                      | 819 ms: 1.14x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 58.7 ms: 1.14x faster                                                     |
| sympy_expand             | 314 ms                                                      | 279 ms: 1.13x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                     |
| logging_format           | 6.76 us                                                     | 6.43 us: 1.05x faster                                                     |
| logging_simple           | 6.22 us                                                     | 5.96 us: 1.04x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 93.2 ms: 1.04x faster                                                     |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.6 ms: 1.04x faster                                                     |
| meteor_contest           | 75.9 ms                                                     | 74.0 ms: 1.03x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.69 ms: 1.01x faster                                                     |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.02x slower                                                     |
| nbody                    | 71.3 ms                                                     | 73.2 ms: 1.03x slower                                                     |
| scimark_fft              | 187 ms                                                      | 194 ms: 1.04x slower                                                      |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 65.4 ms: 1.05x slower                                                     |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                     |
| create_gc_cycles         | 800 us                                                      | 883 us: 1.10x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                     |
| coverage                 | 39.0 ms                                                     | 45.2 ms: 1.16x slower                                                     |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                              |

Benchmark hidden because not significant (5): pathlib, xml_etree_generate, python_startup, pidigits, json
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240702-3.14.0a0-2302696/bm-20240702-pythonperf1-amd64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown