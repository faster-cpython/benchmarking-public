# Results vs. 3.10.4

- fork: python
- ref: 6343486eb60ac5a9e154
- machine: windows-amd64
- commit hash: 6343486
- commit date: 2024-07-02
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| tornado_http   | 108 ms                                                      | 81.5 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 255 ms: 2.06x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 539 ms: 2.06x faster                                                       |
| async_tree_none         | 435 ms                                                      | 213 ms: 2.04x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 380 ms: 1.68x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.95x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.3 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 79.9 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.4 ms: 1.24x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.11x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.3 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.99 ms: 1.53x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.32x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.6 ms: 1.09x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.9 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.8 ms: 1.01x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| mako            | 9.03 ms                                                     | 7.64 ms: 1.18x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.9 ms: 1.14x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.01x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 255 ms: 2.06x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 539 ms: 2.06x faster                                                       |
| async_tree_none          | 435 ms                                                      | 213 ms: 2.04x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 380 ms: 1.68x faster                                                       |
| pylint                   | 350 ms                                                      | 211 ms: 1.66x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.4 ms: 1.56x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 476 ms: 1.54x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.99 ms: 1.53x faster                                                      |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                       |
| go                       | 139 ms                                                      | 92.9 ms: 1.50x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 64.7 ns: 1.46x faster                                                      |
| generators               | 32.4 ms                                                     | 22.6 ms: 1.43x faster                                                      |
| richards                 | 42.4 ms                                                     | 29.7 ms: 1.43x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.2 ms: 1.43x faster                                                      |
| deepcopy                 | 255 us                                                      | 183 us: 1.40x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.52 sec: 1.39x faster                                                     |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.38x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 889 us: 1.37x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.8 ms: 1.35x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.29 ms: 1.34x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.4 ms: 1.33x faster                                                      |
| tornado_http             | 108 ms                                                      | 81.5 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.32x faster                                                       |
| pyflate                  | 409 ms                                                      | 311 ms: 1.32x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.37 sec: 1.30x faster                                                     |
| scimark_sor              | 106 ms                                                      | 83.9 ms: 1.27x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 767 us: 1.25x faster                                                       |
| regex_compile            | 106 ms                                                      | 85.4 ms: 1.24x faster                                                      |
| pycparser                | 930 ms                                                      | 759 ms: 1.23x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 51.2 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.1 ms: 1.21x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.1 ms: 1.19x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.64 ms: 1.18x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.18x faster                                                      |
| thrift                   | 617 us                                                      | 527 us: 1.17x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.9 ms: 1.14x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 67.6 ms: 1.14x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 34.9 ms: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                     |
| regex_dna                | 136 ms                                                      | 122 ms: 1.11x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 185 ms: 1.11x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 535 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| float                    | 61.7 ms                                                     | 56.3 ms: 1.09x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.6 ms: 1.09x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                     |
| coroutines               | 16.0 ms                                                     | 14.9 ms: 1.07x faster                                                      |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.9 ms: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.70 us: 1.01x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.26 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| python_startup           | 20.6 ms                                                     | 20.8 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.3 ms: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 66.1 ms: 1.06x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.54 ms: 1.10x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.99 ms: 1.10x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.0 ms: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                       |
| fannkuch                 | 256 ms                                                      | 285 ms: 1.12x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 892 us: 1.12x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 17.3 ms: 1.12x slower                                                      |
| nbody                    | 71.3 ms                                                     | 79.9 ms: 1.12x slower                                                      |
| scimark_fft              | 187 ms                                                      | 211 ms: 1.13x slower                                                       |
| coverage                 | 39.0 ms                                                     | 45.2 ms: 1.16x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.97 ms: 1.26x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240702-3.14.0a0-6343486/bm-20240702-pythonperf1-amd64-python-6343486eb60ac5a9e154-3.14.0a0-6343486.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown