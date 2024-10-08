# Results vs. 3.10.4

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-amd64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.05x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.09x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                      |
| tornado_http   | 108 ms                                                      | 84.3 ms: 1.28x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 205 ms: 2.12x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 525 ms: 2.11x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 250 ms: 2.10x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.99x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.0 ms: 1.40x faster                                                      |
| float          | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.5 ms: 1.17x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 20.8 ms: 1.35x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.86 ms: 1.56x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 173 us: 1.56x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 130 us: 1.41x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.33x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 37.4 ms: 1.19x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.8 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.16 ms: 1.75x faster                                                      |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.1 ms: 1.09x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 45.2 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                       |
| async_tree_none          | 435 ms                                                      | 205 ms: 2.12x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 525 ms: 2.11x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 250 ms: 2.10x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 15.8 us: 1.82x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.16 ms: 1.75x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.5 ms: 1.70x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.8 ns: 1.67x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.8 ms: 1.59x faster                                                      |
| pyflate                  | 409 ms                                                      | 258 ms: 1.59x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 465 ms: 1.58x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.86 ms: 1.56x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 173 us: 1.56x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.0 ms: 1.54x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 40.7 ms: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.6 ms: 1.52x faster                                                      |
| pylint                   | 350 ms                                                      | 231 ms: 1.52x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 804 us: 1.51x faster                                                       |
| go                       | 139 ms                                                      | 94.2 ms: 1.48x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.47x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                      |
| deepcopy                 | 255 us                                                      | 181 us: 1.41x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 130 us: 1.41x faster                                                       |
| nbody                    | 71.3 ms                                                     | 51.0 ms: 1.40x faster                                                      |
| richards                 | 42.4 ms                                                     | 30.6 ms: 1.39x faster                                                      |
| generators               | 32.4 ms                                                     | 23.6 ms: 1.37x faster                                                      |
| float                    | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.33x faster                                                     |
| tornado_http             | 108 ms                                                      | 84.3 ms: 1.28x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.12 ms: 1.28x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 953 ms: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 464 ms: 1.28x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.42 sec: 1.25x faster                                                     |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.62 ms: 1.24x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.79 us: 1.23x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 70.3 ms: 1.22x faster                                                      |
| scimark_sor              | 106 ms                                                      | 88.9 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 804 us: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 37.4 ms: 1.19x faster                                                      |
| regex_compile            | 106 ms                                                      | 90.5 ms: 1.17x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| fannkuch                 | 256 ms                                                      | 221 ms: 1.16x faster                                                       |
| sympy_sum                | 107 ms                                                      | 92.9 ms: 1.15x faster                                                      |
| pycparser                | 930 ms                                                      | 822 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.6 ms: 1.12x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.9 ms: 1.11x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.1 ms: 1.09x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.19 us: 1.09x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.09x faster                                                     |
| logging_simple           | 6.22 us                                                     | 5.74 us: 1.08x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 190 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 181 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| 2to3                     | 246 ms                                                      | 233 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.8 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.6 ms: 1.03x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 74.6 ms: 1.01x faster                                                      |
| sympy_expand             | 314 ms                                                      | 313 ms: 1.00x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 45.2 ms: 1.10x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.6 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 901 us: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.48 ms: 1.14x slower                                                      |
| async_generators         | 222 ms                                                      | 257 ms: 1.16x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.1 ms: 1.18x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 20.8 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (2): json, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-pythonperf1-amd64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown