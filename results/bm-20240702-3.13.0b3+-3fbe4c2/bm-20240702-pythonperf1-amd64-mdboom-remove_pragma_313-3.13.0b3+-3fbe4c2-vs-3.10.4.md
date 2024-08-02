# Results vs. 3.10.4

- fork: mdboom
- ref: remove_pragma_313
- machine: windows-amd64
- commit hash: 3fbe4c2
- commit date: 2024-07-02
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 213 ms: 1.15x faster                                                     |
| chameleon      | 5.79 ms                                                     | 4.68 ms: 1.24x faster                                                    |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                   |
| html5lib       | 51.0 ms                                                     | 38.2 ms: 1.33x faster                                                    |
| tornado_http   | 108 ms                                                      | 82.4 ms: 1.31x faster                                                    |
| Geometric mean | (ref)                                                       | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 217 ms: 2.00x faster                                                     |
| async_tree_memoization  | 526 ms                                                      | 267 ms: 1.97x faster                                                     |
| async_tree_io           | 1.11 sec                                                    | 586 ms: 1.89x faster                                                     |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                                     |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.0 ms: 1.23x faster                                                    |
| nbody          | 71.3 ms                                                     | 69.0 ms: 1.03x faster                                                    |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                       | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.4 ms: 1.30x faster                                                    |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                     |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                       | 1.10x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.67 ms: 1.62x faster                                                    |
| pickle_pure_python   | 270 us                                                      | 181 us: 1.49x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 124 us: 1.48x faster                                                     |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.22x faster                                                   |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                    |
| xml_etree_parse      | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                    |
| xml_etree_generate   | 55.5 ms                                                     | 53.9 ms: 1.03x faster                                                    |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.21x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.38 ms: 1.42x faster                                                    |
| genshi_text     | 19.8 ms                                                     | 14.9 ms: 1.33x faster                                                    |
| django_template | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                    |
| genshi_xml      | 41.0 ms                                                     | 32.3 ms: 1.27x faster                                                    |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.28x faster                                                     |
| deltablue                | 4.19 ms                                                     | 1.93 ms: 2.17x faster                                                    |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.00x faster                                                     |
| async_tree_memoization   | 526 ms                                                      | 267 ms: 1.97x faster                                                     |
| async_tree_io            | 1.11 sec                                                    | 586 ms: 1.89x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 52.2 ns: 1.81x faster                                                    |
| raytrace                 | 273 ms                                                      | 158 ms: 1.73x faster                                                     |
| richards_super           | 52.2 ms                                                     | 30.2 ms: 1.73x faster                                                    |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                                     |
| comprehensions           | 16.5 us                                                     | 9.95 us: 1.66x faster                                                    |
| go                       | 139 ms                                                      | 84.8 ms: 1.64x faster                                                    |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                                    |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                                    |
| json_dumps               | 9.16 ms                                                     | 5.67 ms: 1.62x faster                                                    |
| richards                 | 42.4 ms                                                     | 26.8 ms: 1.58x faster                                                    |
| hexiom                   | 5.74 ms                                                     | 3.68 ms: 1.56x faster                                                    |
| sqlglot_parse            | 1.22 ms                                                     | 780 us: 1.56x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 55.1 ms: 1.56x faster                                                    |
| asyncio_tcp              | 732 ms                                                      | 474 ms: 1.55x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 982 us: 1.50x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 181 us: 1.49x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 124 us: 1.48x faster                                                     |
| pyflate                  | 409 ms                                                      | 280 ms: 1.46x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.3 ms: 1.42x faster                                                    |
| mako                     | 9.03 ms                                                     | 6.38 ms: 1.42x faster                                                    |
| scimark_sor              | 106 ms                                                      | 75.3 ms: 1.41x faster                                                    |
| pycparser                | 930 ms                                                      | 665 ms: 1.40x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 45.1 ms: 1.39x faster                                                    |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.56 sec: 1.35x faster                                                   |
| html5lib                 | 51.0 ms                                                     | 38.2 ms: 1.33x faster                                                    |
| genshi_text              | 19.8 ms                                                     | 14.9 ms: 1.33x faster                                                    |
| django_template          | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                    |
| tornado_http             | 108 ms                                                      | 82.4 ms: 1.31x faster                                                    |
| regex_compile            | 106 ms                                                      | 81.4 ms: 1.30x faster                                                    |
| deepcopy_memo            | 28.8 us                                                     | 22.1 us: 1.30x faster                                                    |
| mdp                      | 1.78 sec                                                    | 1.37 sec: 1.30x faster                                                   |
| mypy2                    | 555 ms                                                      | 429 ms: 1.29x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 32.3 ms: 1.27x faster                                                    |
| bench_thread_pool        | 958 us                                                      | 761 us: 1.26x faster                                                     |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                    |
| sympy_sum                | 107 ms                                                      | 86.0 ms: 1.24x faster                                                    |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.24x faster                                                    |
| pprint_pformat           | 1.22 sec                                                    | 987 ms: 1.24x faster                                                     |
| chameleon                | 5.79 ms                                                     | 4.68 ms: 1.24x faster                                                    |
| float                    | 61.7 ms                                                     | 50.0 ms: 1.23x faster                                                    |
| coroutines               | 16.0 ms                                                     | 13.0 ms: 1.23x faster                                                    |
| spectral_norm            | 77.3 ms                                                     | 63.0 ms: 1.23x faster                                                    |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.22x faster                                                   |
| pprint_safe_repr         | 592 ms                                                      | 483 ms: 1.22x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                    |
| sqlglot_normalize        | 205 ms                                                      | 172 ms: 1.19x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 56.5 ms: 1.18x faster                                                    |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                   |
| deepcopy                 | 255 us                                                      | 219 us: 1.16x faster                                                     |
| sympy_str                | 194 ms                                                      | 167 ms: 1.16x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 34.2 ms: 1.16x faster                                                    |
| 2to3                     | 246 ms                                                      | 213 ms: 1.15x faster                                                     |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.11x faster                                                    |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.45 ms: 1.11x faster                                                    |
| logging_format           | 6.76 us                                                     | 6.12 us: 1.10x faster                                                    |
| sympy_expand             | 314 ms                                                      | 286 ms: 1.10x faster                                                     |
| logging_simple           | 6.22 us                                                     | 5.68 us: 1.10x faster                                                    |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.08x faster                                                     |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.05x faster                                                    |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                    |
| xml_etree_parse          | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                                    |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                    |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                    |
| nbody                    | 71.3 ms                                                     | 69.0 ms: 1.03x faster                                                    |
| xml_etree_generate       | 55.5 ms                                                     | 53.9 ms: 1.03x faster                                                    |
| fannkuch                 | 256 ms                                                      | 248 ms: 1.03x faster                                                     |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                     |
| pathlib                  | 75.7 ms                                                     | 76.7 ms: 1.01x slower                                                    |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                    |
| async_generators         | 222 ms                                                      | 229 ms: 1.04x slower                                                     |
| bench_mp_pool            | 62.0 ms                                                     | 65.7 ms: 1.06x slower                                                    |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                    |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                    |
| create_gc_cycles         | 800 us                                                      | 901 us: 1.13x slower                                                     |
| coverage                 | 39.0 ms                                                     | 45.7 ms: 1.17x slower                                                    |
| telco                    | 3.94 ms                                                     | 4.68 ms: 1.19x slower                                                    |
| thrift                   | 617 us                                                      | 8.44 ms: 13.67x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                             |

Benchmark hidden because not significant (2): python_startup, regex_v8
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240702-3.13.0b3+-3fbe4c2/bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown