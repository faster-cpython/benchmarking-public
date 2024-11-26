# Results vs. 3.10.4

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-amd64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.198x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 253 ms: 1.03x slower                                                       |
| docutils       | 1.92 sec                                                    | 1.95 sec: 1.01x slower                                                     |
| html5lib       | 51.0 ms                                                     | 41.7 ms: 1.23x faster                                                      |
| tornado_http   | 108 ms                                                      | 98.2 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 217 ms: 2.00x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 565 ms: 1.96x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 282 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.4 ms: 1.44x faster                                                      |
| float          | 61.7 ms                                                     | 47.2 ms: 1.31x faster                                                      |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_compile  | 106 ms                                                      | 95.7 ms: 1.11x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.84 ms: 1.57x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.30 sec: 1.28x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 147 us: 1.24x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.94 us: 1.02x faster                                                      |
| pickle_list          | 2.75 us                                                     | 2.72 us: 1.01x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 95.8 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.8 us: 1.03x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.24 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.99 ms: 1.81x faster                                                      |
| django_template | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 19.1 ms: 1.03x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 47.3 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                       |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.00x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 565 ms: 1.96x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 282 ms: 1.87x faster                                                       |
| mako                     | 9.03 ms                                                     | 4.99 ms: 1.81x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 16.2 us: 1.77x faster                                                      |
| scimark_sor              | 106 ms                                                      | 61.9 ms: 1.72x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 384 ms: 1.66x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.2 ns: 1.63x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.84 ms: 1.57x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.6 ms: 1.56x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 40.6 ms: 1.54x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 55.7 ms: 1.54x faster                                                      |
| go                       | 139 ms                                                      | 91.9 ms: 1.51x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 52.6 ms: 1.47x faster                                                      |
| nbody                    | 71.3 ms                                                     | 49.4 ms: 1.44x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                      |
| generators               | 32.4 ms                                                     | 23.2 ms: 1.40x faster                                                      |
| deepcopy                 | 255 us                                                      | 186 us: 1.37x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 887 us: 1.37x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.54 sec: 1.37x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                       |
| richards_super           | 52.2 ms                                                     | 38.6 ms: 1.35x faster                                                      |
| raytrace                 | 273 ms                                                      | 202 ms: 1.35x faster                                                       |
| pyflate                  | 409 ms                                                      | 310 ms: 1.32x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 923 ms: 1.32x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 450 ms: 1.32x faster                                                       |
| float                    | 61.7 ms                                                     | 47.2 ms: 1.31x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.11 ms: 1.29x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.30 sec: 1.28x faster                                                     |
| sqlglot_transpile        | 1.48 ms                                                     | 1.17 ms: 1.26x faster                                                      |
| pylint                   | 350 ms                                                      | 279 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 147 us: 1.24x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.5 ms: 1.23x faster                                                      |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 759 ms: 1.23x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.7 ms: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.2 ms: 1.17x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| regex_compile            | 106 ms                                                      | 95.7 ms: 1.11x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.61 sec: 1.11x faster                                                     |
| tornado_http             | 108 ms                                                      | 98.2 ms: 1.10x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 673 ms: 1.09x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 5.28 ms: 1.09x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 19.1 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                      |
| sympy_sum                | 107 ms                                                      | 104 ms: 1.03x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.1 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.63 us: 1.02x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.94 us: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                       |
| pickle_list              | 2.75 us                                                     | 2.72 us: 1.01x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.15 us: 1.01x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 95.8 ms: 1.01x faster                                                      |
| fannkuch                 | 256 ms                                                      | 254 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.4 ms: 1.01x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 205 ms: 1.00x faster                                                       |
| sympy_str                | 194 ms                                                      | 196 ms: 1.01x slower                                                       |
| docutils                 | 1.92 sec                                                    | 1.95 sec: 1.01x slower                                                     |
| sympy_integrate          | 15.3 ms                                                     | 15.6 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| 2to3                     | 246 ms                                                      | 253 ms: 1.03x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.8 us: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.24 us: 1.06x slower                                                      |
| sympy_expand             | 314 ms                                                      | 334 ms: 1.06x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 81.3 ms: 1.07x slower                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 42.9 ms: 1.08x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.46 ms: 1.13x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 47.3 ms: 1.15x slower                                                      |
| async_generators         | 222 ms                                                      | 260 ms: 1.17x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.5 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.6 ms: 1.27x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.93 ms: 1.37x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 88.9 ms: 1.43x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 58.5 ns: 1.47x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.38 ms: 1.73x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (1): json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1-amd64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.198x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown