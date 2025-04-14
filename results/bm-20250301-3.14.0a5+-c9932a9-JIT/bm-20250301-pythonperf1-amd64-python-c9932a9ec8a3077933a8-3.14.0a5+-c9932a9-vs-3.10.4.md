# Results vs. 3.10.4

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.256x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.13x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 218 ms: 2.42x faster                                                        |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.35x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 346 ms: 1.84x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.1 ms: 1.31x faster                                                       |
| nbody          | 71.3 ms                                                     | 60.0 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.7 ms: 1.27x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                       |
| regex_dna      | 136 ms                                                      | 125 ms: 1.09x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 15.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 114 us: 1.61x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.93 ms: 1.32x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.6 ms: 1.07x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.66 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.93 us: 1.08x slower                                                       |
| pickle               | 6.85 us                                                     | 7.90 us: 1.15x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.25 us: 1.18x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 21.1 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.34 ms: 1.69x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.11x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 218 ms: 2.42x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.37x faster                                                       |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.35x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 346 ms: 1.84x faster                                                        |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.34 ms: 1.69x faster                                                       |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 114 us: 1.61x faster                                                        |
| go                       | 139 ms                                                      | 87.4 ms: 1.59x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.1 ms: 1.53x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 486 ms: 1.51x faster                                                        |
| pyflate                  | 409 ms                                                      | 274 ms: 1.49x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 63.7 ns: 1.48x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.1 ms: 1.47x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 841 us: 1.45x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 20.1 us: 1.43x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.9 ms: 1.42x faster                                                       |
| raytrace                 | 273 ms                                                      | 193 ms: 1.42x faster                                                        |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.38x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.0 ms: 1.33x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.8 ms: 1.32x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.93 ms: 1.32x faster                                                       |
| float                    | 61.7 ms                                                     | 47.1 ms: 1.31x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.39 ms: 1.31x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.09 ms: 1.30x faster                                                       |
| pycparser                | 930 ms                                                      | 730 ms: 1.27x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.2 ms: 1.27x faster                                                       |
| regex_compile            | 106 ms                                                      | 83.7 ms: 1.27x faster                                                       |
| scimark_sor              | 106 ms                                                      | 84.5 ms: 1.26x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.7 ms: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.6 ms: 1.23x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                        |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.23x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 999 ms: 1.22x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.3 ms: 1.21x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.8 ms: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.0 ms: 1.20x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.19x faster                                                      |
| nbody                    | 71.3 ms                                                     | 60.0 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 521 us: 1.18x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.7 ms: 1.18x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 504 ms: 1.17x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 848 us: 1.13x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.13x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.8 ms: 1.12x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.8 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| regex_dna                | 136 ms                                                      | 125 ms: 1.09x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.6 ms: 1.07x faster                                                       |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.66 us: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.0 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 245 ms: 1.04x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 197 ms: 1.04x faster                                                        |
| sympy_expand             | 314 ms                                                      | 303 ms: 1.04x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.0 ms: 1.03x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.2 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                        |
| logging_format           | 6.76 us                                                     | 7.01 us: 1.04x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 41.4 ns: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.57 us: 1.06x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.93 us: 1.08x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.32 ms: 1.10x slower                                                       |
| async_generators         | 222 ms                                                      | 251 ms: 1.13x slower                                                        |
| pickle                   | 6.85 us                                                     | 7.90 us: 1.15x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.25 us: 1.18x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 21.1 us: 1.23x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.3 ms: 1.24x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.3 ms: 1.39x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250301-3.14.0a5+-c9932a9-JIT/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.256x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown