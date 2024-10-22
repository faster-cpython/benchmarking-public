# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-amd64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                      |
| tornado_http   | 108 ms                                                      | 81.5 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 536 ms: 2.07x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 255 ms: 2.07x faster                                                       |
| async_tree_none         | 435 ms                                                      | 212 ms: 2.06x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.67x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.96x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 78.5 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.0 ms: 1.19x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.97 ms: 1.53x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 204 us: 1.32x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.23x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.6 ms: 1.09x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.5 ms: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.0 ms: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.1 ms: 1.02x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.37 ms: 1.23x faster                                                      |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.4 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.2 ms: 1.10x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.16x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 536 ms: 2.07x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 255 ms: 2.07x faster                                                       |
| async_tree_none          | 435 ms                                                      | 212 ms: 2.06x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.90x faster                                                      |
| pylint                   | 350 ms                                                      | 209 ms: 1.68x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.67x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 474 ms: 1.55x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.97 ms: 1.53x faster                                                      |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.6 ms: 1.51x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 63.5 ns: 1.49x faster                                                      |
| generators               | 32.4 ms                                                     | 22.2 ms: 1.46x faster                                                      |
| go                       | 139 ms                                                      | 97.0 ms: 1.43x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                      |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.38x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 878 us: 1.38x faster                                                       |
| richards                 | 42.4 ms                                                     | 30.7 ms: 1.38x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.36x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.56 sec: 1.35x faster                                                     |
| tornado_http             | 108 ms                                                      | 81.5 ms: 1.33x faster                                                      |
| pyflate                  | 409 ms                                                      | 309 ms: 1.32x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 204 us: 1.32x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 66.2 ms: 1.30x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.51 ms: 1.27x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.37 ms: 1.23x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.23x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 793 us: 1.21x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.6 ms: 1.21x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.4 ms: 1.20x faster                                                      |
| pycparser                | 930 ms                                                      | 773 ms: 1.20x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 52.0 ms: 1.20x faster                                                      |
| regex_compile            | 106 ms                                                      | 89.0 ms: 1.19x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.18x faster                                                      |
| scimark_sor              | 106 ms                                                      | 90.7 ms: 1.17x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.16x faster                                                     |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.7 ms: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                     |
| sympy_str                | 194 ms                                                      | 173 ms: 1.12x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 185 ms: 1.11x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.10x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 37.2 ms: 1.10x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 52.0 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.6 ms: 1.09x faster                                                      |
| float                    | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 546 ms: 1.08x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 72.4 ms: 1.07x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                     |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.9 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.7 ms: 1.04x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.60 us: 1.02x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 74.1 ms: 1.02x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 75.7 ms: 1.00x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.1 ms: 1.02x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.5 ms: 1.02x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.0 ms: 1.05x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 65.2 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.93 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.54 ms: 1.09x slower                                                      |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                       |
| nbody                    | 71.3 ms                                                     | 78.5 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 896 us: 1.12x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| scimark_fft              | 187 ms                                                      | 216 ms: 1.15x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.2 ms: 1.18x slower                                                      |
| fannkuch                 | 256 ms                                                      | 304 ms: 1.19x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.86 ms: 1.23x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (2): regex_v8, logging_simple
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown