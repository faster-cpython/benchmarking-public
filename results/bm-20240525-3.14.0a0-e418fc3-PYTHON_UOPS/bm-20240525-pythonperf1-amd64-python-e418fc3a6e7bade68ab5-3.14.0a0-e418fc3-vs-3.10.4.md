# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.11x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 239 ms: 1.03x faster                                                       |
| chameleon      | 5.79 ms                                                     | 5.39 ms: 1.07x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.85 sec: 1.04x faster                                                     |
| html5lib       | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                      |
| tornado_http   | 108 ms                                                      | 87.2 ms: 1.24x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 290 ms: 1.81x faster                                                       |
| async_tree_none         | 435 ms                                                      | 242 ms: 1.80x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 627 ms: 1.77x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 410 ms: 1.56x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.73x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 81.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| regex_compile  | 106 ms                                                      | 111 ms: 1.04x slower                                                       |
| regex_v8       | 15.4 ms                                                     | 17.1 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.82 ms: 1.57x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.4 ms: 1.10x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.53 sec: 1.10x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 167 us: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.72 us: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 67.4 ms: 1.04x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.26 us: 1.06x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.02 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.54 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 38.9 ms: 1.06x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 119 us: 2.82x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 290 ms: 1.81x faster                                                       |
| async_tree_none          | 435 ms                                                      | 242 ms: 1.80x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 627 ms: 1.77x faster                                                       |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.65x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.82 ms: 1.57x faster                                                      |
| richards_super           | 52.2 ms                                                     | 33.5 ms: 1.56x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 410 ms: 1.56x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.70 ms: 1.55x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.37 sec: 1.55x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 488 ms: 1.50x faster                                                       |
| pylint                   | 350 ms                                                      | 236 ms: 1.49x faster                                                       |
| raytrace                 | 273 ms                                                      | 188 ms: 1.45x faster                                                       |
| richards                 | 42.4 ms                                                     | 30.0 ms: 1.41x faster                                                      |
| chaos                    | 61.7 ms                                                     | 45.7 ms: 1.35x faster                                                      |
| go                       | 139 ms                                                      | 104 ms: 1.33x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 927 us: 1.31x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.17 ms: 1.26x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                                      |
| tornado_http             | 108 ms                                                      | 87.2 ms: 1.24x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 77.4 ns: 1.22x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                      |
| pyflate                  | 409 ms                                                      | 339 ms: 1.21x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.54 ms: 1.20x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 52.3 ms: 1.20x faster                                                      |
| thrift                   | 617 us                                                      | 517 us: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| scimark_sor              | 106 ms                                                      | 93.2 ms: 1.14x faster                                                      |
| comprehensions           | 16.5 us                                                     | 14.5 us: 1.14x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.57 sec: 1.14x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 848 us: 1.13x faster                                                       |
| pycparser                | 930 ms                                                      | 831 ms: 1.12x faster                                                       |
| float                    | 61.7 ms                                                     | 55.9 ms: 1.10x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.9 ms: 1.10x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.4 ms: 1.10x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.53 sec: 1.10x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 167 us: 1.10x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                      |
| chameleon                | 5.79 ms                                                     | 5.39 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 38.9 ms: 1.06x faster                                                      |
| sympy_sum                | 107 ms                                                      | 102 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.72 us: 1.04x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.17 sec: 1.04x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.85 sec: 1.04x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 83.1 ms: 1.03x faster                                                      |
| 2to3                     | 246 ms                                                      | 239 ms: 1.03x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 577 ms: 1.03x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 38.9 ms: 1.02x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.9 ms: 1.02x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.64 us: 1.02x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| sympy_str                | 194 ms                                                      | 197 ms: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.26 us: 1.02x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 67.4 ms: 1.04x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 79.0 ms: 1.04x slower                                                      |
| deepcopy                 | 255 us                                                      | 266 us: 1.04x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.9 ms: 1.04x slower                                                      |
| regex_compile            | 106 ms                                                      | 111 ms: 1.04x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 79.1 ms: 1.04x slower                                                      |
| spectral_norm            | 77.3 ms                                                     | 80.8 ms: 1.05x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.26 us: 1.06x slower                                                      |
| sympy_expand             | 314 ms                                                      | 337 ms: 1.07x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 71.7 ms: 1.08x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.7 ms: 1.08x slower                                                      |
| deepcopy_memo            | 28.8 us                                                     | 31.2 us: 1.08x slower                                                      |
| scimark_fft              | 187 ms                                                      | 204 ms: 1.09x slower                                                       |
| fannkuch                 | 256 ms                                                      | 280 ms: 1.10x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 68.1 ms: 1.10x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.02 us: 1.10x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.1 ms: 1.11x slower                                                      |
| nbody                    | 71.3 ms                                                     | 81.2 ms: 1.14x slower                                                      |
| async_generators         | 222 ms                                                      | 254 ms: 1.15x slower                                                       |
| coverage                 | 39.0 ms                                                     | 44.8 ms: 1.15x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 926 us: 1.16x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.29 ms: 1.21x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.04 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (4): python_startup, flaskblogging, hexiom, logging_simple
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown