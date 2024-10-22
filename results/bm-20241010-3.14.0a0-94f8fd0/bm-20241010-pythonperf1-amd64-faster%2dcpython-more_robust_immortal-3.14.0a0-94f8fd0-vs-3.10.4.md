# Results vs. 3.10.4

- fork: faster-cpython
- ref: more_robust_immortal
- machine: windows-amd64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                               |
| html5lib       | 51.0 ms                                                     | 42.2 ms: 1.21x faster                                                                |
| tornado_http   | 108 ms                                                      | 94.8 ms: 1.14x faster                                                                |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 212 ms: 2.05x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 273 ms: 1.93x faster                                                                 |
| async_tree_io           | 1.11 sec                                                    | 593 ms: 1.87x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 398 ms: 1.60x faster                                                                 |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.8 ms: 1.12x faster                                                                |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                                 |
| nbody          | 71.3 ms                                                     | 80.7 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                                 |
| regex_compile  | 106 ms                                                      | 90.1 ms: 1.18x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.34 ms: 1.45x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.25x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                                 |
| xml_etree_process    | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 93.9 ms: 1.03x faster                                                                |
| tomli_loads          | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                               |
| unpickle             | 9.09 us                                                     | 9.35 us: 1.03x slower                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.9 ms: 1.03x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 58.7 ms: 1.06x slower                                                                |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                                |
| unpickle_list        | 2.71 us                                                     | 2.89 us: 1.07x slower                                                                |
| pickle_list          | 2.75 us                                                     | 2.93 us: 1.07x slower                                                                |
| pickle               | 6.85 us                                                     | 7.45 us: 1.09x slower                                                                |
| pickle_dict          | 17.2 us                                                     | 19.2 us: 1.12x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                                |
| django_template | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 38.2 ms: 1.08x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 212 ms: 2.05x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 273 ms: 1.93x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 593 ms: 1.87x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 398 ms: 1.60x faster                                                                 |
| go                       | 139 ms                                                      | 87.4 ms: 1.59x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 60.1 ns: 1.58x faster                                                                |
| pylint                   | 350 ms                                                      | 228 ms: 1.54x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 57.4 ms: 1.49x faster                                                                |
| generators               | 32.4 ms                                                     | 21.7 ms: 1.49x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.34 ms: 1.45x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 19.9 us: 1.44x faster                                                                |
| richards_super           | 52.2 ms                                                     | 36.6 ms: 1.43x faster                                                                |
| raytrace                 | 273 ms                                                      | 192 ms: 1.42x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                                |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.39x faster                                                                |
| sqlglot_parse            | 1.22 ms                                                     | 912 us: 1.33x faster                                                                 |
| hexiom                   | 5.74 ms                                                     | 4.32 ms: 1.33x faster                                                                |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                                 |
| mako                     | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                                                |
| richards                 | 42.4 ms                                                     | 32.5 ms: 1.31x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 48.3 ms: 1.30x faster                                                                |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.29x faster                                                                |
| pyflate                  | 409 ms                                                      | 319 ms: 1.28x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.25x faster                                                                 |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                                 |
| pycparser                | 930 ms                                                      | 756 ms: 1.23x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.9 ms: 1.22x faster                                                                |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.73 sec: 1.22x faster                                                               |
| html5lib                 | 51.0 ms                                                     | 42.2 ms: 1.21x faster                                                                |
| scimark_sor              | 106 ms                                                      | 88.0 ms: 1.21x faster                                                                |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                                 |
| sympy_sum                | 107 ms                                                      | 90.2 ms: 1.19x faster                                                                |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                                 |
| regex_compile            | 106 ms                                                      | 90.1 ms: 1.18x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.65 us: 1.16x faster                                                                |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                                |
| bench_thread_pool        | 958 us                                                      | 838 us: 1.14x faster                                                                 |
| tornado_http             | 108 ms                                                      | 94.8 ms: 1.14x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 44.2 ms: 1.14x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                                |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.13x faster                                                               |
| float                    | 61.7 ms                                                     | 54.8 ms: 1.12x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 69.3 ms: 1.11x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                                |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                                 |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                               |
| django_template          | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 38.2 ms: 1.08x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 552 ms: 1.07x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                                |
| sqlglot_optimize         | 39.8 ms                                                     | 37.6 ms: 1.06x faster                                                                |
| asyncio_tcp              | 732 ms                                                      | 695 ms: 1.05x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 64.1 ms: 1.04x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 93.9 ms: 1.03x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                               |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.66 ms: 1.02x faster                                                                |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                                 |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                                 |
| meteor_contest           | 75.9 ms                                                     | 76.4 ms: 1.01x slower                                                                |
| unpack_sequence          | 39.6 ns                                                     | 40.2 ns: 1.01x slower                                                                |
| logging_format           | 6.76 us                                                     | 6.91 us: 1.02x slower                                                                |
| unpickle                 | 9.09 us                                                     | 9.35 us: 1.03x slower                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.9 ms: 1.03x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.45 us: 1.04x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 58.7 ms: 1.06x slower                                                                |
| pathlib                  | 75.7 ms                                                     | 80.3 ms: 1.06x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                                |
| unpickle_list            | 2.71 us                                                     | 2.89 us: 1.07x slower                                                                |
| pickle_list              | 2.75 us                                                     | 2.93 us: 1.07x slower                                                                |
| python_startup           | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                                                |
| scimark_fft              | 187 ms                                                      | 202 ms: 1.08x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.09x slower                                                                |
| pickle                   | 6.85 us                                                     | 7.45 us: 1.09x slower                                                                |
| fannkuch                 | 256 ms                                                      | 279 ms: 1.09x slower                                                                 |
| pickle_dict              | 17.2 us                                                     | 19.2 us: 1.12x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 69.6 ms: 1.12x slower                                                                |
| nbody                    | 71.3 ms                                                     | 80.7 ms: 1.13x slower                                                                |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.15x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 934 us: 1.17x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.93 ms: 1.25x slower                                                                |
| coverage                 | 39.0 ms                                                     | 48.9 ms: 1.25x slower                                                                |
| json                     | 3.14 ms                                                     | 4.15 ms: 1.32x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                                         |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown