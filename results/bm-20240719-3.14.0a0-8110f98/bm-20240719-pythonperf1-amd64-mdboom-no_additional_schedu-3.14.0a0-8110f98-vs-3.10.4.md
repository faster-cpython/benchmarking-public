# Results vs. 3.10.4

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 8110f98
- commit date: 2024-07-19
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| tornado_http   | 108 ms                                                      | 91.4 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 538 ms: 2.06x faster                                                       |
| async_tree_none         | 435 ms                                                      | 213 ms: 2.04x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 258 ms: 2.04x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 382 ms: 1.67x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.94x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.0 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 75.5 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.3 ms: 1.27x faster                                                      |
| regex_dna      | 136 ms                                                      | 127 ms: 1.07x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.95 ms: 1.54x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 199 us: 1.36x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.26x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 39.9 ms: 1.11x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.2 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.5 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.5 ms: 1.05x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                      |
| mako            | 9.03 ms                                                     | 7.54 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 538 ms: 2.06x faster                                                       |
| async_tree_none          | 435 ms                                                      | 213 ms: 2.04x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 258 ms: 2.04x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.08 ms: 2.01x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 382 ms: 1.67x faster                                                       |
| pylint                   | 350 ms                                                      | 211 ms: 1.66x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.0 ms: 1.63x faster                                                      |
| raytrace                 | 273 ms                                                      | 173 ms: 1.58x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 60.6 ns: 1.56x faster                                                      |
| go                       | 139 ms                                                      | 89.2 ms: 1.56x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.95 ms: 1.54x faster                                                      |
| generators               | 32.4 ms                                                     | 21.7 ms: 1.50x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.5 ms: 1.49x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.9 ms: 1.47x faster                                                      |
| deepcopy                 | 255 us                                                      | 178 us: 1.44x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.41x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 861 us: 1.41x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 522 ms: 1.40x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 62.2 ms: 1.38x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.37x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 199 us: 1.36x faster                                                       |
| pyflate                  | 409 ms                                                      | 302 ms: 1.35x faster                                                       |
| scimark_sor              | 106 ms                                                      | 78.9 ms: 1.35x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.60 sec: 1.32x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.40 sec: 1.27x faster                                                     |
| regex_compile            | 106 ms                                                      | 83.3 ms: 1.27x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.26x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.5 ms: 1.26x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                      |
| pycparser                | 930 ms                                                      | 755 ms: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 86.9 ms: 1.23x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.6 ms: 1.23x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.54 ms: 1.20x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                      |
| tornado_http             | 108 ms                                                      | 91.4 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 815 us: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 529 us: 1.17x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 66.7 ms: 1.16x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 34.6 ms: 1.15x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 39.9 ms: 1.11x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 185 ms: 1.11x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 534 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                       |
| float                    | 61.7 ms                                                     | 56.0 ms: 1.10x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.2 ms: 1.09x faster                                                      |
| regex_dna                | 136 ms                                                      | 127 ms: 1.07x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 93.8 ms: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.66 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 76.8 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.2 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.5 ms: 1.04x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.5 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.86 ms: 1.05x slower                                                      |
| nbody                    | 71.3 ms                                                     | 75.5 ms: 1.06x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.6 ms: 1.07x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 67.4 ms: 1.09x slower                                                      |
| scimark_fft              | 187 ms                                                      | 204 ms: 1.09x slower                                                       |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                       |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 890 us: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.4 ms: 1.19x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.79 ms: 1.22x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                               |

Benchmark hidden because not significant (3): json, logging_simple, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240719-3.14.0a0-8110f98/bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-8110f98.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown