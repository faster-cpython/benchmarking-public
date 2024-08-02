# Results vs. 3.10.4

- fork: python
- ref: 68e279b37aae3019979a
- machine: windows-amd64
- commit hash: 68e279b
- commit date: 2024-07-07
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                      |
| tornado_http   | 108 ms                                                      | 84.4 ms: 1.28x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 519 ms: 2.14x faster                                                       |
| async_tree_none         | 435 ms                                                      | 206 ms: 2.11x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 252 ms: 2.09x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 382 ms: 1.67x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.99x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| nbody          | 71.3 ms                                                     | 52.2 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.7 ms: 1.21x faster                                                      |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 19.9 ms: 1.29x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.68 ms: 1.61x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 174 us: 1.55x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 127 us: 1.44x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 37.1 ms: 1.20x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.8 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.1 ms: 1.03x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.9 ms: 1.10x faster                                                      |
| django_template | 28.9 ms                                                     | 27.1 ms: 1.06x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.2 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 519 ms: 2.14x faster                                                       |
| async_tree_none          | 435 ms                                                      | 206 ms: 2.11x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 252 ms: 2.09x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 15.7 us: 1.83x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.10 ms: 1.77x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.7 ms: 1.69x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.3 ns: 1.68x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 382 ms: 1.67x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.68 ms: 1.61x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                                      |
| pyflate                  | 409 ms                                                      | 258 ms: 1.59x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.2 ms: 1.57x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.36 sec: 1.55x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 174 us: 1.55x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.1 ms: 1.54x faster                                                      |
| pylint                   | 350 ms                                                      | 228 ms: 1.54x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 477 ms: 1.53x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.9 ms: 1.51x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 805 us: 1.51x faster                                                       |
| raytrace                 | 273 ms                                                      | 184 ms: 1.49x faster                                                       |
| go                       | 139 ms                                                      | 93.6 ms: 1.48x faster                                                      |
| richards                 | 42.4 ms                                                     | 29.3 ms: 1.45x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 127 us: 1.44x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                      |
| deepcopy                 | 255 us                                                      | 180 us: 1.42x faster                                                       |
| generators               | 32.4 ms                                                     | 22.8 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| nbody                    | 71.3 ms                                                     | 52.2 ms: 1.37x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                     |
| tornado_http             | 108 ms                                                      | 84.4 ms: 1.28x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 952 ms: 1.28x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 466 ms: 1.27x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.15 ms: 1.26x faster                                                      |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.25x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 68.5 ms: 1.25x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 769 us: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.64 ms: 1.24x faster                                                      |
| regex_compile            | 106 ms                                                      | 87.7 ms: 1.21x faster                                                      |
| scimark_sor              | 106 ms                                                      | 87.9 ms: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.21x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 37.1 ms: 1.20x faster                                                      |
| thrift                   | 617 us                                                      | 518 us: 1.19x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                     |
| pycparser                | 930 ms                                                      | 792 ms: 1.17x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.17x faster                                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 92.2 ms: 1.16x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.1 ms: 1.13x faster                                                      |
| fannkuch                 | 256 ms                                                      | 230 ms: 1.11x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 17.9 ms: 1.10x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 186 ms: 1.10x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.7 ms: 1.08x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.28 us: 1.08x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.8 ms: 1.07x faster                                                      |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.84 us: 1.06x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.1 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                      |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.7 ms: 1.02x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.1 ms: 1.03x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 44.2 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 68.7 ms: 1.11x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 902 us: 1.13x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.48 ms: 1.14x slower                                                      |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.4 ms: 1.19x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 19.9 ms: 1.29x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (2): pidigits, pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240707-3.14.0a0-68e279b-JIT/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown