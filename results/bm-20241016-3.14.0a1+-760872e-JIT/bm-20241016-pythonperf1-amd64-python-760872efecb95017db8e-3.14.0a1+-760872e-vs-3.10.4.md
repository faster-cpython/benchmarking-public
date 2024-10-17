# Results vs. 3.10.4

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-amd64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| html5lib       | 51.0 ms                                                     | 39.7 ms: 1.28x faster                                                       |
| tornado_http   | 108 ms                                                      | 98.1 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 554 ms: 2.00x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_none         | 435 ms                                                      | 234 ms: 1.86x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 388 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 54.7 ms: 1.30x faster                                                       |
| float          | 61.7 ms                                                     | 47.5 ms: 1.30x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.5 ms: 1.16x faster                                                       |
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 15.6 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.37 ms: 1.44x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 197 us: 1.37x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 142 us: 1.29x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.71 us: 1.02x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 95.6 ms: 1.01x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.03x slower                                                       |
| pickle               | 6.85 us                                                     | 7.21 us: 1.05x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.87 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.9 ms: 1.16x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.94 ms: 1.83x faster                                                       |
| django_template | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.3 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 554 ms: 2.00x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_none          | 435 ms                                                      | 234 ms: 1.86x faster                                                        |
| mako                     | 9.03 ms                                                     | 4.94 ms: 1.83x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.4 us: 1.76x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.5 ns: 1.68x faster                                                       |
| scimark_sor              | 106 ms                                                      | 64.0 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 388 ms: 1.64x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.1 ms: 1.59x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 39.8 ms: 1.57x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 55.4 ms: 1.55x faster                                                       |
| go                       | 139 ms                                                      | 91.2 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.7 ms: 1.48x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.37 ms: 1.44x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 54.5 ms: 1.42x faster                                                       |
| pyflate                  | 409 ms                                                      | 289 ms: 1.41x faster                                                        |
| generators               | 32.4 ms                                                     | 23.0 ms: 1.41x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.53 sec: 1.38x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 197 us: 1.37x faster                                                        |
| richards_super           | 52.2 ms                                                     | 38.5 ms: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 897 us: 1.35x faster                                                        |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 935 ms: 1.30x faster                                                        |
| nbody                    | 71.3 ms                                                     | 54.7 ms: 1.30x faster                                                       |
| float                    | 61.7 ms                                                     | 47.5 ms: 1.30x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 142 us: 1.29x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 458 ms: 1.29x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.7 ms: 1.28x faster                                                       |
| raytrace                 | 273 ms                                                      | 215 ms: 1.27x faster                                                        |
| pylint                   | 350 ms                                                      | 279 ms: 1.26x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.18 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.18 ms: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.4 ms: 1.25x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.0 ms: 1.25x faster                                                       |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                                       |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.22x faster                                                        |
| thrift                   | 617 us                                                      | 513 us: 1.20x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.5 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 827 us: 1.16x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.56 sec: 1.14x faster                                                      |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                        |
| fannkuch                 | 256 ms                                                      | 231 ms: 1.11x faster                                                        |
| tornado_http             | 108 ms                                                      | 98.1 ms: 1.10x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 5.21 ms: 1.10x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 665 ms: 1.10x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.0 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.5 ms: 1.05x faster                                                       |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                       |
| sympy_sum                | 107 ms                                                      | 103 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.62 us: 1.02x faster                                                       |
| pickle_list              | 2.75 us                                                     | 2.71 us: 1.02x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 95.6 ms: 1.01x faster                                                       |
| sympy_str                | 194 ms                                                      | 192 ms: 1.01x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.17 us: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 75.5 ms: 1.01x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 207 ms: 1.01x slower                                                        |
| regex_v8                 | 15.4 ms                                                     | 15.6 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.03x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 15.8 ms: 1.03x slower                                                       |
| sympy_expand             | 314 ms                                                      | 325 ms: 1.03x slower                                                        |
| pickle                   | 6.85 us                                                     | 7.21 us: 1.05x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.87 us: 1.06x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 80.5 ms: 1.06x slower                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 43.2 ms: 1.08x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.34 ms: 1.10x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.3 ms: 1.13x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.9 ms: 1.16x slower                                                       |
| async_generators         | 222 ms                                                      | 260 ms: 1.17x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.0 ms: 1.23x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.8 ms: 1.45x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 59.3 ns: 1.50x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.41 ms: 1.76x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (5): genshi_text, unpickle, regex_effbot, docutils, 2to3
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1-amd64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown