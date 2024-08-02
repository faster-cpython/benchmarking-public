# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                        |
| chameleon      | 5.79 ms                                                     | 5.12 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.84 sec: 1.05x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.6 ms: 1.23x faster                                                       |
| tornado_http   | 108 ms                                                      | 87.8 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 593 ms: 1.87x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 282 ms: 1.87x faster                                                        |
| async_tree_none         | 435 ms                                                      | 233 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 400 ms: 1.59x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.79x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| nbody          | 71.3 ms                                                     | 73.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.81 ms: 1.58x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 156 us: 1.18x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.46 sec: 1.15x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.4 ms: 1.13x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.51 us: 1.07x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.86 us: 1.04x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.84 us: 1.05x slower                                                       |
| pickle               | 6.85 us                                                     | 7.17 us: 1.05x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.34 ms: 1.23x faster                                                       |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.6 ms: 1.13x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 593 ms: 1.87x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 282 ms: 1.87x faster                                                        |
| async_tree_none          | 435 ms                                                      | 233 ms: 1.87x faster                                                        |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.65x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.55 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 400 ms: 1.59x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.81 ms: 1.58x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.2 ms: 1.57x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 475 ms: 1.54x faster                                                        |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                      |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                        |
| richards                 | 42.4 ms                                                     | 29.3 ms: 1.45x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.1 ms: 1.43x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 68.3 ns: 1.39x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 881 us: 1.38x faster                                                        |
| go                       | 139 ms                                                      | 102 ms: 1.36x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                       |
| pyflate                  | 409 ms                                                      | 321 ms: 1.28x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                        |
| coroutines               | 16.0 ms                                                     | 12.6 ms: 1.27x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.6 ms: 1.26x faster                                                       |
| comprehensions           | 16.5 us                                                     | 13.3 us: 1.24x faster                                                       |
| scimark_sor              | 106 ms                                                      | 85.7 ms: 1.24x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.24x faster                                                      |
| tornado_http             | 108 ms                                                      | 87.8 ms: 1.23x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.34 ms: 1.23x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.6 ms: 1.23x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.0 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 156 us: 1.18x faster                                                        |
| float                    | 61.7 ms                                                     | 52.6 ms: 1.17x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 73.6 ms: 1.17x faster                                                       |
| mypy2                    | 555 ms                                                      | 480 ms: 1.16x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.46 sec: 1.15x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.1 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                        |
| chameleon                | 5.79 ms                                                     | 5.12 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.4 ms: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 17.6 ms: 1.13x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 5.18 ms: 1.11x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 536 ms: 1.10x faster                                                        |
| sympy_sum                | 107 ms                                                      | 98.4 ms: 1.09x faster                                                       |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.07x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.51 us: 1.07x faster                                                       |
| aiohttp                  | 995 us                                                      | 933 us: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                                       |
| pycparser                | 930 ms                                                      | 876 ms: 1.06x faster                                                        |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 14.6 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.84 sec: 1.05x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 74.1 ms: 1.04x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 38.3 ms: 1.04x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.56 us: 1.03x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.16 us: 1.02x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 28.5 us: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.16 us: 1.01x faster                                                       |
| sympy_str                | 194 ms                                                      | 194 ms: 1.00x faster                                                        |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 76.4 ms: 1.01x slower                                                       |
| scimark_fft              | 187 ms                                                      | 189 ms: 1.01x slower                                                        |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                       |
| nbody                    | 71.3 ms                                                     | 73.8 ms: 1.03x slower                                                       |
| fannkuch                 | 256 ms                                                      | 265 ms: 1.04x slower                                                        |
| pickle_list              | 2.75 us                                                     | 2.86 us: 1.04x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.84 us: 1.05x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.17 us: 1.05x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.3 ms: 1.05x slower                                                       |
| sympy_expand             | 314 ms                                                      | 335 ms: 1.07x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 18.4 us: 1.07x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 67.0 ms: 1.08x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.94 ms: 1.08x slower                                                       |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                        |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.12x slower                                                       |
| coverage                 | 39.0 ms                                                     | 43.7 ms: 1.12x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 917 us: 1.15x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.70 ms: 1.19x slower                                                       |
| thrift                   | 617 us                                                      | 9.56 ms: 15.49x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (7): python_startup, xml_etree_iterparse, regex_compile, nqueens, deepcopy, pathlib, json_loads
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown