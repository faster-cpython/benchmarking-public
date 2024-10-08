# Results vs. 3.10.4

- fork: python
- ref: 498376d7a7d6f704f22a
- machine: windows-amd64
- commit hash: 498376d
- commit date: 2024-08-02
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 240 ms: 1.02x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.84 sec: 1.05x faster                                                     |
| html5lib       | 51.0 ms                                                     | 41.0 ms: 1.24x faster                                                      |
| tornado_http   | 108 ms                                                      | 96.1 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 212 ms: 2.05x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 551 ms: 2.01x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 392 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.8 ms: 1.43x faster                                                      |
| float          | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.4 ms: 1.19x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.99 ms: 1.53x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 181 us: 1.49x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 37.5 ms: 1.19x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.9 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.96 ms: 1.82x faster                                                      |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.9 ms: 1.11x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 39.0 ms: 1.05x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 121 us: 2.79x faster                                                       |
| async_tree_none          | 435 ms                                                      | 212 ms: 2.05x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 551 ms: 2.01x faster                                                       |
| mako                     | 9.03 ms                                                     | 4.96 ms: 1.82x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 16.2 us: 1.78x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.36 ms: 1.78x faster                                                      |
| scimark_sor              | 106 ms                                                      | 59.9 ms: 1.77x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 46.1 ms: 1.68x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.5 ns: 1.67x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 392 ms: 1.63x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                      |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.0 ms: 1.58x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                      |
| generators               | 32.4 ms                                                     | 20.8 ms: 1.56x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 55.6 ms: 1.54x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.99 ms: 1.53x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.5 ms: 1.53x faster                                                      |
| richards_super           | 52.2 ms                                                     | 34.5 ms: 1.51x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 181 us: 1.49x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 834 us: 1.46x faster                                                       |
| raytrace                 | 273 ms                                                      | 188 ms: 1.45x faster                                                       |
| nbody                    | 71.3 ms                                                     | 49.8 ms: 1.43x faster                                                      |
| deepcopy                 | 255 us                                                      | 183 us: 1.40x faster                                                       |
| pylint                   | 350 ms                                                      | 252 ms: 1.39x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.52 sec: 1.39x faster                                                     |
| richards                 | 42.4 ms                                                     | 30.6 ms: 1.39x faster                                                      |
| go                       | 139 ms                                                      | 101 ms: 1.38x faster                                                       |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.37x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.07 ms: 1.31x faster                                                      |
| pycparser                | 930 ms                                                      | 726 ms: 1.28x faster                                                       |
| scimark_fft              | 187 ms                                                      | 148 ms: 1.27x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 475 ms: 1.25x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.0 ms: 1.24x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 983 ms: 1.24x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.24x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.69 ms: 1.22x faster                                                      |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.4 ms: 1.19x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 37.5 ms: 1.19x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 43.1 ms: 1.17x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                      |
| fannkuch                 | 256 ms                                                      | 220 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 825 us: 1.16x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 638 ms: 1.15x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| tornado_http             | 108 ms                                                      | 96.1 ms: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.9 ms: 1.11x faster                                                      |
| sympy_sum                | 107 ms                                                      | 97.3 ms: 1.10x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.1 ms: 1.08x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.9 ms: 1.08x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.36 us: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 39.0 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.95 us: 1.05x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.84 sec: 1.05x faster                                                     |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.9 ms: 1.04x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.7 ms: 1.04x faster                                                      |
| sympy_str                | 194 ms                                                      | 188 ms: 1.04x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                      |
| 2to3                     | 246 ms                                                      | 240 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| sympy_expand             | 314 ms                                                      | 332 ms: 1.06x slower                                                       |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 82.1 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 919 us: 1.15x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.54 ms: 1.15x slower                                                      |
| async_generators         | 222 ms                                                      | 256 ms: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 73.7 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.1 ms: 1.21x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240802-3.14.0a0-498376d-JIT/bm-20240802-pythonperf1-amd64-python-498376d7a7d6f704f22a-3.14.0a0-498376d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown