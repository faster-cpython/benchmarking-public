# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-amd64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                      |
| tornado_http   | 108 ms                                                      | 83.8 ms: 1.29x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 205 ms: 2.12x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 251 ms: 2.09x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 530 ms: 2.09x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 381 ms: 1.67x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.99x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| nbody          | 71.3 ms                                                     | 53.4 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.1 ms: 1.19x faster                                                      |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.79 ms: 1.58x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 174 us: 1.55x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 130 us: 1.41x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.2 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.17 ms: 1.75x faster                                                      |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.9 ms: 1.11x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 46.9 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.93x faster                                                       |
| async_tree_none          | 435 ms                                                      | 205 ms: 2.12x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 251 ms: 2.09x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 530 ms: 2.09x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.5 us: 1.86x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.17 ms: 1.75x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 44.5 ms: 1.74x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.5 ns: 1.67x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 381 ms: 1.67x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                                      |
| pyflate                  | 409 ms                                                      | 256 ms: 1.60x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.8 ms: 1.59x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.79 ms: 1.58x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 465 ms: 1.57x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.2 ms: 1.55x faster                                                      |
| richards_super           | 52.2 ms                                                     | 33.6 ms: 1.55x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 174 us: 1.55x faster                                                       |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                                       |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.6 ms: 1.52x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 800 us: 1.52x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.41 sec: 1.49x faster                                                     |
| go                       | 139 ms                                                      | 93.0 ms: 1.49x faster                                                      |
| deepcopy                 | 255 us                                                      | 177 us: 1.45x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                      |
| richards                 | 42.4 ms                                                     | 29.8 ms: 1.42x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 130 us: 1.41x faster                                                       |
| generators               | 32.4 ms                                                     | 23.5 ms: 1.38x faster                                                      |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| nbody                    | 71.3 ms                                                     | 53.4 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                      |
| tornado_http             | 108 ms                                                      | 83.8 ms: 1.29x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 950 ms: 1.28x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 464 ms: 1.27x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.27x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.76 us: 1.25x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.18 ms: 1.25x faster                                                      |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.61 ms: 1.25x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.5 ms: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 513 us: 1.20x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 797 us: 1.20x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.1 ms: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                      |
| sympy_sum                | 107 ms                                                      | 92.6 ms: 1.15x faster                                                      |
| fannkuch                 | 256 ms                                                      | 222 ms: 1.15x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 74.6 ms: 1.15x faster                                                      |
| pycparser                | 930 ms                                                      | 811 ms: 1.15x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 35.5 ms: 1.12x faster                                                      |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.08 us: 1.11x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.9 ms: 1.11x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.63 us: 1.11x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.5 ms: 1.10x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 188 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.2 ms: 1.06x faster                                                      |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.2 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.01x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.2 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 898 us: 1.12x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.49 ms: 1.14x slower                                                      |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.9 ms: 1.14x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (4): json, pathlib, pidigits, regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown