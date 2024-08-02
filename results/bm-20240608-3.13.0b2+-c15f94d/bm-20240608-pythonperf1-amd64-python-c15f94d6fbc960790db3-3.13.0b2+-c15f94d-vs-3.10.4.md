# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 208 ms: 1.18x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.81 ms: 1.20x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.5 ms: 1.44x faster                                                       |
| tornado_http   | 108 ms                                                      | 82.1 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 217 ms: 2.01x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 265 ms: 1.99x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 580 ms: 1.91x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.1 ms: 1.23x faster                                                       |
| nbody          | 71.3 ms                                                     | 64.9 ms: 1.10x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.1 ms: 1.36x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 17.6 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.60 ms: 1.64x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 172 us: 1.57x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 124 us: 1.48x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 37.1 ms: 1.20x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.45 us: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                       |
| pickle               | 6.85 us                                                     | 7.16 us: 1.05x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.41 ms: 1.41x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.8 ms: 1.29x faster                                                       |
| django_template | 28.9 ms                                                     | 22.6 ms: 1.28x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.28x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.88 ms: 2.23x faster                                                       |
| async_tree_none          | 435 ms                                                      | 217 ms: 2.01x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 265 ms: 1.99x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 580 ms: 1.91x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 52.6 ns: 1.80x faster                                                       |
| raytrace                 | 273 ms                                                      | 159 ms: 1.72x faster                                                        |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                        |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.69x faster                                                       |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                       |
| go                       | 139 ms                                                      | 83.4 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.60 ms: 1.64x faster                                                       |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 755 us: 1.61x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 172 us: 1.57x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 54.7 ms: 1.57x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.71 ms: 1.55x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 477 ms: 1.54x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 964 us: 1.53x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 124 us: 1.48x faster                                                        |
| pyflate                  | 409 ms                                                      | 278 ms: 1.47x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.45x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 35.5 ms: 1.44x faster                                                       |
| scimark_sor              | 106 ms                                                      | 73.9 ms: 1.44x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.1 ms: 1.43x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.41 ms: 1.41x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.0 ms: 1.39x faster                                                       |
| regex_compile            | 106 ms                                                      | 78.1 ms: 1.36x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                       |
| mypy2                    | 555 ms                                                      | 418 ms: 1.33x faster                                                        |
| tornado_http             | 108 ms                                                      | 82.1 ms: 1.32x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.2 ms: 1.32x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 22.0 us: 1.31x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.37 sec: 1.30x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 31.8 ms: 1.29x faster                                                       |
| django_template          | 28.9 ms                                                     | 22.6 ms: 1.28x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 965 ms: 1.26x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 471 ms: 1.26x faster                                                        |
| sympy_sum                | 107 ms                                                      | 85.3 ms: 1.26x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.25x faster                                                       |
| float                    | 61.7 ms                                                     | 50.1 ms: 1.23x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 63.4 ms: 1.22x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 787 us: 1.22x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 32.8 ms: 1.21x faster                                                       |
| sympy_str                | 194 ms                                                      | 160 ms: 1.21x faster                                                        |
| chameleon                | 5.79 ms                                                     | 4.81 ms: 1.20x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 37.1 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 55.9 ms: 1.19x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 172 ms: 1.19x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                      |
| pycparser                | 930 ms                                                      | 786 ms: 1.18x faster                                                        |
| 2to3                     | 246 ms                                                      | 208 ms: 1.18x faster                                                        |
| deepcopy                 | 255 us                                                      | 218 us: 1.17x faster                                                        |
| sympy_expand             | 314 ms                                                      | 272 ms: 1.16x faster                                                        |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.40 ms: 1.14x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.98 us: 1.12x faster                                                       |
| aiohttp                  | 995 us                                                      | 898 us: 1.11x faster                                                        |
| scimark_fft              | 187 ms                                                      | 170 ms: 1.10x faster                                                        |
| nbody                    | 71.3 ms                                                     | 64.9 ms: 1.10x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.17 us: 1.10x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.69 us: 1.09x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.45 us: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 244 ms: 1.05x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                                       |
| python_startup           | 20.6 ms                                                     | 20.2 ms: 1.02x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.03 sec: 1.00x slower                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 225 ms: 1.02x slower                                                        |
| pickle                   | 6.85 us                                                     | 7.16 us: 1.05x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 65.0 ms: 1.05x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.89 us: 1.05x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                       |
| coverage                 | 39.0 ms                                                     | 43.3 ms: 1.11x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 900 us: 1.12x slower                                                        |
| regex_v8                 | 15.4 ms                                                     | 17.6 ms: 1.14x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.68 ms: 1.19x slower                                                       |
| thrift                   | 617 us                                                      | 7.90 ms: 12.80x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, pathlib
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown