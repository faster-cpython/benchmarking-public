# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.07x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.96 ms: 1.17x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                      |
| html5lib       | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                                       |
| tornado_http   | 108 ms                                                      | 86.3 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 226 ms: 1.92x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 595 ms: 1.86x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 400 ms: 1.59x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.82x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.4 ms: 1.42x faster                                                       |
| float          | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.0 ms: 1.20x faster                                                       |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 16.9 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.77 ms: 1.59x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 171 us: 1.58x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.46x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.50 us: 1.07x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.7 ms: 1.07x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.4 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.02x slower                                                       |
| pickle               | 6.85 us                                                     | 7.18 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.07 ms: 1.78x faster                                                       |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 44.6 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                        |
| async_tree_none          | 435 ms                                                      | 226 ms: 1.92x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 595 ms: 1.86x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.07 ms: 1.78x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 44.4 ms: 1.74x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.5 ns: 1.67x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.3 ms: 1.62x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 400 ms: 1.59x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.77 ms: 1.59x faster                                                       |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 171 us: 1.58x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 474 ms: 1.55x faster                                                        |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 800 us: 1.52x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 41.4 ms: 1.51x faster                                                       |
| generators               | 32.4 ms                                                     | 21.5 ms: 1.51x faster                                                       |
| pylint                   | 350 ms                                                      | 235 ms: 1.49x faster                                                        |
| go                       | 139 ms                                                      | 93.6 ms: 1.48x faster                                                       |
| richards                 | 42.4 ms                                                     | 28.6 ms: 1.48x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.46x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.4 ms: 1.45x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.45x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.1 us: 1.43x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.03 ms: 1.43x faster                                                       |
| nbody                    | 71.3 ms                                                     | 50.4 ms: 1.42x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                                       |
| float                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                      |
| scimark_sor              | 106 ms                                                      | 81.1 ms: 1.31x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 947 ms: 1.29x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 462 ms: 1.28x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                       |
| scimark_fft              | 187 ms                                                      | 148 ms: 1.27x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                                      |
| tornado_http             | 108 ms                                                      | 86.3 ms: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.24x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 69.0 ms: 1.24x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.66 ms: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 762 ms: 1.22x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                       |
| fannkuch                 | 256 ms                                                      | 211 ms: 1.21x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| regex_compile            | 106 ms                                                      | 88.0 ms: 1.20x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.96 ms: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 824 us: 1.16x faster                                                        |
| mypy2                    | 555 ms                                                      | 484 ms: 1.15x faster                                                        |
| sympy_sum                | 107 ms                                                      | 93.9 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.1 ms: 1.13x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.7 ms: 1.09x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.08x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.24 us: 1.08x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.08x faster                                                       |
| deepcopy                 | 255 us                                                      | 237 us: 1.08x faster                                                        |
| logging_simple           | 6.22 us                                                     | 5.78 us: 1.08x faster                                                       |
| aiohttp                  | 995 us                                                      | 929 us: 1.07x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.50 us: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.7 ms: 1.07x faster                                                       |
| 2to3                     | 246 ms                                                      | 231 ms: 1.07x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 52.4 ms: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.09 us: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.8 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 312 ms: 1.01x faster                                                        |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.02x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.18 us: 1.05x slower                                                       |
| python_startup           | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 44.6 ms: 1.09x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 16.9 ms: 1.09x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.4 ms: 1.12x slower                                                       |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.49 ms: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 924 us: 1.15x slower                                                        |
| coverage                 | 39.0 ms                                                     | 46.8 ms: 1.20x slower                                                       |
| thrift                   | 617 us                                                      | 9.10 ms: 14.74x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (4): unpickle_list, pathlib, pidigits, pickle_list
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown