# Results vs. 3.10.4

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-amd64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.11x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                    |
| html5lib       | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                     |
| tornado_http   | 108 ms                                                      | 83.5 ms: 1.30x faster                                                     |
| Geometric mean | (ref)                                                       | 1.20x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 206 ms: 2.11x faster                                                      |
| async_tree_memoization  | 526 ms                                                      | 261 ms: 2.02x faster                                                      |
| async_tree_io           | 1.11 sec                                                    | 571 ms: 1.94x faster                                                      |
| async_tree_cpu_io_mixed | 638 ms                                                      | 390 ms: 1.63x faster                                                      |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.2 ms: 1.14x faster                                                     |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                      |
| nbody          | 71.3 ms                                                     | 82.1 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                      |
| regex_compile  | 106 ms                                                      | 89.2 ms: 1.19x faster                                                     |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                     |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                       | 1.13x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.14 ms: 1.49x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.25x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                     |
| tomli_loads          | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                    |
| xml_etree_parse      | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                     |
| xml_etree_generate   | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                     |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                     |
| pickle               | 6.85 us                                                     | 7.15 us: 1.04x slower                                                     |
| unpickle             | 9.09 us                                                     | 9.50 us: 1.05x slower                                                     |
| pickle_list          | 2.75 us                                                     | 2.91 us: 1.06x slower                                                     |
| pickle_dict          | 17.2 us                                                     | 19.2 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                              |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.3 ms: 1.03x slower                                                     |
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.84 ms: 1.32x faster                                                     |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                     |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                     |
| genshi_xml      | 41.0 ms                                                     | 36.7 ms: 1.12x faster                                                     |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.06x faster                                                      |
| async_tree_none          | 435 ms                                                      | 206 ms: 2.11x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 261 ms: 2.02x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 571 ms: 1.94x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                     |
| go                       | 139 ms                                                      | 84.6 ms: 1.64x faster                                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 390 ms: 1.63x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 462 ms: 1.59x faster                                                      |
| pylint                   | 350 ms                                                      | 224 ms: 1.57x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 61.7 ns: 1.53x faster                                                     |
| generators               | 32.4 ms                                                     | 21.1 ms: 1.53x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.14 ms: 1.49x faster                                                     |
| raytrace                 | 273 ms                                                      | 184 ms: 1.49x faster                                                      |
| richards_super           | 52.2 ms                                                     | 35.5 ms: 1.47x faster                                                     |
| chaos                    | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 59.9 ms: 1.43x faster                                                     |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 20.2 us: 1.43x faster                                                     |
| sqlglot_parse            | 1.22 ms                                                     | 868 us: 1.40x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.36x faster                                                     |
| deepcopy                 | 255 us                                                      | 190 us: 1.35x faster                                                      |
| richards                 | 42.4 ms                                                     | 31.5 ms: 1.35x faster                                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.58 sec: 1.34x faster                                                    |
| hexiom                   | 5.74 ms                                                     | 4.33 ms: 1.33x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 47.2 ms: 1.32x faster                                                     |
| mako                     | 9.03 ms                                                     | 6.84 ms: 1.32x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                      |
| tornado_http             | 108 ms                                                      | 83.5 ms: 1.30x faster                                                     |
| pyflate                  | 409 ms                                                      | 316 ms: 1.29x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                     |
| mdp                      | 1.78 sec                                                    | 1.40 sec: 1.27x faster                                                    |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.25x faster                                                      |
| pycparser                | 930 ms                                                      | 751 ms: 1.24x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.1 ms: 1.23x faster                                                     |
| thrift                   | 617 us                                                      | 512 us: 1.21x faster                                                      |
| sympy_sum                | 107 ms                                                      | 89.1 ms: 1.20x faster                                                     |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                     |
| regex_compile            | 106 ms                                                      | 89.2 ms: 1.19x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 807 us: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 65.3 ms: 1.18x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                     |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.17x faster                                                     |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.1 ms: 1.17x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                    |
| float                    | 61.7 ms                                                     | 54.2 ms: 1.14x faster                                                     |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 36.7 ms: 1.12x faster                                                     |
| 2to3                     | 246 ms                                                      | 220 ms: 1.11x faster                                                      |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.1 ms: 1.10x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                    |
| pprint_safe_repr         | 592 ms                                                      | 541 ms: 1.09x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                    |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.08x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                     |
| nqueens                  | 66.6 ms                                                     | 63.7 ms: 1.05x faster                                                     |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                     |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.03x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 74.2 ms: 1.02x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.67 ms: 1.02x faster                                                     |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                     |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.1 ms: 1.03x slower                                                     |
| xml_etree_generate       | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                     |
| python_startup           | 20.6 ms                                                     | 21.3 ms: 1.03x slower                                                     |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                     |
| pickle                   | 6.85 us                                                     | 7.15 us: 1.04x slower                                                     |
| unpickle                 | 9.09 us                                                     | 9.50 us: 1.05x slower                                                     |
| pickle_list              | 2.75 us                                                     | 2.91 us: 1.06x slower                                                     |
| scimark_fft              | 187 ms                                                      | 199 ms: 1.06x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.08x slower                                                     |
| bench_mp_pool            | 62.0 ms                                                     | 67.4 ms: 1.09x slower                                                     |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 43.2 ns: 1.09x slower                                                     |
| create_gc_cycles         | 800 us                                                      | 888 us: 1.11x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.2 us: 1.12x slower                                                     |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.12x slower                                                     |
| fannkuch                 | 256 ms                                                      | 289 ms: 1.13x slower                                                      |
| nbody                    | 71.3 ms                                                     | 82.1 ms: 1.15x slower                                                     |
| coverage                 | 39.0 ms                                                     | 46.6 ms: 1.19x slower                                                     |
| telco                    | 3.94 ms                                                     | 5.04 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                              |

Benchmark hidden because not significant (3): xml_etree_iterparse, logging_simple, unpickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown