# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 242 ms: 1.02x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.85 sec: 1.04x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.1 ms: 1.21x faster                                                      |
| tornado_http   | 108 ms                                                      | 95.2 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 214 ms: 2.04x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 553 ms: 2.01x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 395 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.1 ms: 1.42x faster                                                      |
| float          | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.0 ms: 1.17x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.96 ms: 1.54x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 182 us: 1.48x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 138 us: 1.33x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 37.6 ms: 1.18x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 95.5 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.05 ms: 1.79x faster                                                      |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.9 ms: 1.10x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 40.0 ms: 1.03x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.23x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.89x faster                                                       |
| async_tree_none          | 435 ms                                                      | 214 ms: 2.04x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 553 ms: 2.01x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.7 us: 1.83x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.05 ms: 1.79x faster                                                      |
| scimark_sor              | 106 ms                                                      | 60.4 ms: 1.76x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.0 ms: 1.72x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 57.2 ns: 1.66x faster                                                      |
| pyflate                  | 409 ms                                                      | 251 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 395 ms: 1.62x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.0 ms: 1.59x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 40.3 ms: 1.55x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.96 ms: 1.54x faster                                                      |
| richards_super           | 52.2 ms                                                     | 35.0 ms: 1.49x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 182 us: 1.48x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.2 ms: 1.46x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 838 us: 1.45x faster                                                       |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                      |
| raytrace                 | 273 ms                                                      | 190 ms: 1.44x faster                                                       |
| nbody                    | 71.3 ms                                                     | 50.1 ms: 1.42x faster                                                      |
| pylint                   | 350 ms                                                      | 248 ms: 1.41x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.51 sec: 1.40x faster                                                     |
| richards                 | 42.4 ms                                                     | 30.4 ms: 1.39x faster                                                      |
| float                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| go                       | 139 ms                                                      | 102 ms: 1.37x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.36x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 138 us: 1.33x faster                                                       |
| deepcopy                 | 255 us                                                      | 193 us: 1.32x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.10 ms: 1.30x faster                                                      |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.28x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 993 ms: 1.23x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 484 ms: 1.22x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.1 ms: 1.21x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 4.79 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                      |
| fannkuch                 | 256 ms                                                      | 214 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 520 us: 1.19x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 37.6 ms: 1.18x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.0 ms: 1.17x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                      |
| pycparser                | 930 ms                                                      | 800 ms: 1.16x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 826 us: 1.16x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 632 ms: 1.16x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| tornado_http             | 108 ms                                                      | 95.2 ms: 1.14x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.9 ms: 1.10x faster                                                      |
| sympy_sum                | 107 ms                                                      | 98.4 ms: 1.09x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 194 ms: 1.06x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.39 us: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.6 ms: 1.06x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.8 ms: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.94 us: 1.05x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.85 sec: 1.04x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 40.0 ms: 1.03x faster                                                      |
| 2to3                     | 246 ms                                                      | 242 ms: 1.02x faster                                                       |
| sympy_str                | 194 ms                                                      | 192 ms: 1.01x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 95.5 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| sympy_expand             | 314 ms                                                      | 334 ms: 1.06x slower                                                       |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 81.4 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 925 us: 1.16x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                                      |
| async_generators         | 222 ms                                                      | 261 ms: 1.18x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 73.7 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240802-3.14.0a0-7aca84e-JIT/bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown