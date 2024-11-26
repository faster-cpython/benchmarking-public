# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-amd64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.186x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.8 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 210 ms: 2.07x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 260 ms: 2.03x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 573 ms: 1.93x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 390 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.2 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                       |
| nbody          | 71.3 ms                                                     | 83.6 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| regex_compile  | 106 ms                                                      | 91.5 ms: 1.16x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.29x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 95.6 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.87 ms: 1.31x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.93x faster                                                       |
| async_tree_none          | 435 ms                                                      | 210 ms: 2.07x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 260 ms: 2.03x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 573 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                      |
| go                       | 139 ms                                                      | 84.7 ms: 1.64x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 390 ms: 1.63x faster                                                       |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.57x faster                                                      |
| pylint                   | 350 ms                                                      | 228 ms: 1.53x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.5 ns: 1.51x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.5 us: 1.48x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.24 ms: 1.47x faster                                                      |
| raytrace                 | 273 ms                                                      | 188 ms: 1.46x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.7 ms: 1.45x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 512 ms: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.39x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 62.3 ms: 1.38x faster                                                      |
| deepcopy                 | 255 us                                                      | 186 us: 1.37x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 891 us: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.34x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.32 ms: 1.33x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.87 ms: 1.31x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.61 sec: 1.31x faster                                                     |
| richards                 | 42.4 ms                                                     | 32.4 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.29x faster                                                       |
| pyflate                  | 409 ms                                                      | 322 ms: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.24x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 759 ms: 1.23x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                      |
| scimark_sor              | 106 ms                                                      | 88.7 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| sympy_sum                | 107 ms                                                      | 90.1 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.1 ms: 1.17x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.17x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.5 ms: 1.16x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.8 ms: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 831 us: 1.15x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 67.4 ms: 1.15x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.4 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                     |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| float                    | 61.7 ms                                                     | 56.2 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 555 ms: 1.07x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.66 ms: 1.02x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 65.2 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.63 us: 1.02x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 95.6 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.3 ms: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                      |
| scimark_fft              | 187 ms                                                      | 195 ms: 1.04x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 79.4 ms: 1.05x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 68.7 ms: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                       |
| fannkuch                 | 256 ms                                                      | 291 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 917 us: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| nbody                    | 71.3 ms                                                     | 83.6 ms: 1.17x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.09 ms: 1.29x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (4): json, xml_etree_iterparse, regex_v8, logging_simple
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1-amd64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.186x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown