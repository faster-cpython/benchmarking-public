# Results vs. 3.10.4

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-amd64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 43.0 ms: 1.19x faster                                                      |
| tornado_http   | 108 ms                                                      | 92.7 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 210 ms: 2.07x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 260 ms: 2.02x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 576 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.9 ms: 1.08x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 87.6 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_compile  | 106 ms                                                      | 93.0 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 218 us: 1.23x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 94.4 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.88 us: 1.05x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.52 us: 1.05x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.07x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| pickle               | 6.85 us                                                     | 7.49 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.7 ms: 1.10x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.23 ms: 1.25x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                      |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                       |
| async_tree_none          | 435 ms                                                      | 210 ms: 2.07x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 260 ms: 2.02x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 576 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                       |
| go                       | 139 ms                                                      | 88.9 ms: 1.56x faster                                                      |
| pylint                   | 350 ms                                                      | 226 ms: 1.55x faster                                                       |
| generators               | 32.4 ms                                                     | 21.4 ms: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 65.9 ns: 1.44x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.8 ms: 1.42x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.50 sec: 1.40x faster                                                     |
| raytrace                 | 273 ms                                                      | 198 ms: 1.38x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.8 ms: 1.38x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 534 ms: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.3 us: 1.34x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 908 us: 1.34x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.5 us: 1.34x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.30x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.6 ms: 1.30x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 67.9 ms: 1.26x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.23 ms: 1.25x faster                                                      |
| pyflate                  | 409 ms                                                      | 329 ms: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.63 ms: 1.24x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 218 us: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.9 ms: 1.23x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 43.0 ms: 1.19x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.4 ms: 1.18x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.52 sec: 1.17x faster                                                     |
| thrift                   | 617 us                                                      | 527 us: 1.17x faster                                                       |
| tornado_http             | 108 ms                                                      | 92.7 ms: 1.17x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.64 us: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 824 us: 1.16x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 43.7 ms: 1.15x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.0 ms: 1.14x faster                                                      |
| regex_compile            | 106 ms                                                      | 93.0 ms: 1.14x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.3 ms: 1.12x faster                                                      |
| scimark_sor              | 106 ms                                                      | 96.2 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| float                    | 61.7 ms                                                     | 56.9 ms: 1.08x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.9 ms: 1.07x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.14 sec: 1.07x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 554 ms: 1.07x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 74.9 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 94.4 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.5 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.84 us: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.6 ms: 1.02x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 78.4 ms: 1.04x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.47 us: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.84 ms: 1.04x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.88 us: 1.05x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 79.5 ms: 1.05x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.52 us: 1.05x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.07x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.5 ms: 1.07x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 42.8 ns: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.09x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.49 us: 1.09x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.7 ms: 1.10x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 884 us: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                       |
| scimark_fft              | 187 ms                                                      | 214 ms: 1.14x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 72.5 ms: 1.17x slower                                                      |
| fannkuch                 | 256 ms                                                      | 307 ms: 1.20x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.9 ms: 1.23x slower                                                      |
| nbody                    | 71.3 ms                                                     | 87.6 ms: 1.23x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.87 ms: 1.24x slower                                                      |
| json                     | 3.14 ms                                                     | 4.15 ms: 1.32x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                               |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown