# Results vs. 3.10.4

- fork: mdboom
- ref: marshal_slice
- machine: windows-amd64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                              |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                               |
| tornado_http   | 108 ms                                                      | 92.9 ms: 1.17x faster                                               |
| Geometric mean | (ref)                                                       | 1.16x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 207 ms: 2.10x faster                                                |
| async_tree_memoization  | 526 ms                                                      | 262 ms: 2.01x faster                                                |
| async_tree_io           | 1.11 sec                                                    | 573 ms: 1.94x faster                                                |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.0 ms: 1.10x faster                                               |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                |
| nbody          | 71.3 ms                                                     | 81.0 ms: 1.14x slower                                               |
| Geometric mean | (ref)                                                       | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                |
| regex_compile  | 106 ms                                                      | 90.4 ms: 1.17x faster                                               |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                               |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                       | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                               |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.26x faster                                                |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                |
| xml_etree_process    | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                               |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                              |
| xml_etree_parse      | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                               |
| unpickle_list        | 2.71 us                                                     | 2.74 us: 1.01x slower                                               |
| unpickle             | 9.09 us                                                     | 9.30 us: 1.02x slower                                               |
| pickle               | 6.85 us                                                     | 7.12 us: 1.04x slower                                               |
| xml_etree_generate   | 55.5 ms                                                     | 58.0 ms: 1.05x slower                                               |
| pickle_list          | 2.75 us                                                     | 2.90 us: 1.06x slower                                               |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                               |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                               |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                               |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.93 ms: 1.30x faster                                               |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                               |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                               |
| genshi_xml      | 41.0 ms                                                     | 35.6 ms: 1.15x faster                                               |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                |
| async_tree_none          | 435 ms                                                      | 207 ms: 2.10x faster                                                |
| async_tree_memoization   | 526 ms                                                      | 262 ms: 2.01x faster                                                |
| async_tree_io            | 1.11 sec                                                    | 573 ms: 1.94x faster                                                |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                |
| go                       | 139 ms                                                      | 87.1 ms: 1.59x faster                                               |
| pylint                   | 350 ms                                                      | 223 ms: 1.57x faster                                                |
| generators               | 32.4 ms                                                     | 20.9 ms: 1.55x faster                                               |
| logging_silent           | 94.6 ns                                                     | 63.1 ns: 1.50x faster                                               |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                               |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                               |
| deepcopy_memo            | 28.8 us                                                     | 20.1 us: 1.43x faster                                               |
| chaos                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                               |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                               |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                                |
| sqlglot_parse            | 1.22 ms                                                     | 880 us: 1.38x faster                                                |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                |
| asyncio_tcp              | 732 ms                                                      | 532 ms: 1.37x faster                                                |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.56 sec: 1.36x faster                                              |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                               |
| richards                 | 42.4 ms                                                     | 32.2 ms: 1.32x faster                                               |
| hexiom                   | 5.74 ms                                                     | 4.37 ms: 1.32x faster                                               |
| scimark_lu               | 85.8 ms                                                     | 65.8 ms: 1.30x faster                                               |
| mako                     | 9.03 ms                                                     | 6.93 ms: 1.30x faster                                               |
| pycparser                | 930 ms                                                      | 720 ms: 1.29x faster                                                |
| pyflate                  | 409 ms                                                      | 319 ms: 1.28x faster                                                |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                               |
| crypto_pyaes             | 62.5 ms                                                     | 49.3 ms: 1.27x faster                                               |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                              |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.26x faster                                                |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                |
| thrift                   | 617 us                                                      | 513 us: 1.20x faster                                                |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                |
| sympy_sum                | 107 ms                                                      | 90.0 ms: 1.19x faster                                               |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.4 ms: 1.18x faster                                               |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                               |
| scimark_sor              | 106 ms                                                      | 90.4 ms: 1.17x faster                                               |
| regex_compile            | 106 ms                                                      | 90.4 ms: 1.17x faster                                               |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                               |
| bench_thread_pool        | 958 us                                                      | 819 us: 1.17x faster                                                |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                               |
| tornado_http             | 108 ms                                                      | 92.9 ms: 1.17x faster                                               |
| genshi_xml               | 41.0 ms                                                     | 35.6 ms: 1.15x faster                                               |
| dulwich_log              | 50.5 ms                                                     | 43.8 ms: 1.15x faster                                               |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                               |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                               |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                              |
| spectral_norm            | 77.3 ms                                                     | 68.8 ms: 1.12x faster                                               |
| float                    | 61.7 ms                                                     | 56.0 ms: 1.10x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                              |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                               |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                |
| xml_etree_process        | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                               |
| pprint_safe_repr         | 592 ms                                                      | 542 ms: 1.09x faster                                                |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                               |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                              |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                               |
| xml_etree_parse          | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                               |
| nqueens                  | 66.6 ms                                                     | 64.6 ms: 1.03x faster                                               |
| unpack_sequence          | 39.6 ns                                                     | 38.5 ns: 1.03x faster                                               |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                |
| meteor_contest           | 75.9 ms                                                     | 76.3 ms: 1.01x slower                                               |
| logging_format           | 6.76 us                                                     | 6.82 us: 1.01x slower                                               |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                |
| unpickle_list            | 2.71 us                                                     | 2.74 us: 1.01x slower                                               |
| logging_simple           | 6.22 us                                                     | 6.33 us: 1.02x slower                                               |
| unpickle                 | 9.09 us                                                     | 9.30 us: 1.02x slower                                               |
| pickle                   | 6.85 us                                                     | 7.12 us: 1.04x slower                                               |
| pathlib                  | 75.7 ms                                                     | 78.8 ms: 1.04x slower                                               |
| xml_etree_generate       | 55.5 ms                                                     | 58.0 ms: 1.05x slower                                               |
| pickle_list              | 2.75 us                                                     | 2.90 us: 1.06x slower                                               |
| python_startup           | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                               |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                               |
| scimark_fft              | 187 ms                                                      | 205 ms: 1.09x slower                                                |
| bench_mp_pool            | 62.0 ms                                                     | 68.9 ms: 1.11x slower                                               |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                               |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                |
| fannkuch                 | 256 ms                                                      | 288 ms: 1.13x slower                                                |
| nbody                    | 71.3 ms                                                     | 81.0 ms: 1.14x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                               |
| create_gc_cycles         | 800 us                                                      | 917 us: 1.15x slower                                                |
| telco                    | 3.94 ms                                                     | 4.84 ms: 1.23x slower                                               |
| coverage                 | 39.0 ms                                                     | 49.2 ms: 1.26x slower                                               |
| json                     | 3.14 ms                                                     | 4.27 ms: 1.36x slower                                               |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_iterparse, scimark_sparse_mat_mult, json_loads
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown