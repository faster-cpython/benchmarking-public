# Results vs. 3.10.4

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: windows-amd64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.195x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 406 ms: 2.73x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.52x faster                                                        |
| async_tree_none         | 435 ms                                                      | 178 ms: 2.44x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 361 ms: 1.76x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.3 ms: 1.33x faster                                                       |
| nbody          | 71.3 ms                                                     | 67.7 ms: 1.05x faster                                                       |
| pidigits       | 149 ms                                                      | 155 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.9 ms: 1.22x faster                                                       |
| regex_dna      | 136 ms                                                      | 129 ms: 1.06x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 17.1 ms: 1.11x slower                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.87 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 220 us: 1.23x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.21x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 7.88 ms: 1.16x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.60 us: 1.04x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 17.1 us: 1.00x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 46.1 ms: 1.04x slower                                                       |
| unpickle             | 9.09 us                                                     | 9.72 us: 1.07x slower                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 104 ms: 1.07x slower                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 70.0 ms: 1.08x slower                                                       |
| pickle               | 6.85 us                                                     | 7.56 us: 1.10x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.14 us: 1.14x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 65.8 ms: 1.19x slower                                                       |
| json_loads           | 14.0 us                                                     | 20.5 us: 1.46x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                       |
| python_startup         | 20.6 ms                                                     | 27.4 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 32.5 ms: 1.26x faster                                                       |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| mako            | 9.03 ms                                                     | 8.33 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 406 ms: 2.73x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.52x faster                                                        |
| async_tree_none          | 435 ms                                                      | 178 ms: 2.44x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 31.6 ms: 2.40x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.98 ms: 2.12x faster                                                       |
| generators               | 32.4 ms                                                     | 17.3 ms: 1.88x faster                                                       |
| go                       | 139 ms                                                      | 77.2 ms: 1.80x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 361 ms: 1.76x faster                                                        |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                        |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                                        |
| richards_super           | 52.2 ms                                                     | 33.6 ms: 1.55x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 26.2 ns: 1.51x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.3 us: 1.49x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 63.9 ns: 1.48x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.46x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 833 us: 1.46x faster                                                        |
| richards                 | 42.4 ms                                                     | 29.4 ms: 1.44x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.6 ms: 1.42x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.05 ms: 1.40x faster                                                       |
| deepcopy                 | 255 us                                                      | 182 us: 1.40x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 525 ms: 1.39x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.15 ms: 1.38x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.37x faster                                                       |
| pyflate                  | 409 ms                                                      | 302 ms: 1.35x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.6 ms: 1.35x faster                                                       |
| float                    | 61.7 ms                                                     | 46.3 ms: 1.33x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                       |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.0 ms: 1.27x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.7 ms: 1.27x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 32.5 ms: 1.26x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.35 sec: 1.24x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 220 us: 1.23x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                       |
| regex_compile            | 106 ms                                                      | 86.9 ms: 1.22x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 63.4 ms: 1.22x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.21x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.2 ms: 1.20x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 52.3 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.6 ms: 1.17x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.88 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.08 sec: 1.13x faster                                                      |
| thrift                   | 617 us                                                      | 552 us: 1.12x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 531 ms: 1.11x faster                                                        |
| sympy_str                | 194 ms                                                      | 178 ms: 1.10x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.5 ms: 1.09x faster                                                       |
| mako                     | 9.03 ms                                                     | 8.33 ms: 1.08x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 889 us: 1.08x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.66 sec: 1.07x faster                                                      |
| regex_dna                | 136 ms                                                      | 129 ms: 1.06x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 194 ms: 1.06x faster                                                        |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                        |
| nbody                    | 71.3 ms                                                     | 67.7 ms: 1.05x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.60 us: 1.04x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 64.0 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.03x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.1 ms: 1.02x faster                                                       |
| pickle_dict              | 17.2 us                                                     | 17.1 us: 1.00x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.76 ms: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 225 ms: 1.01x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.34 us: 1.02x slower                                                       |
| xml_etree_process        | 44.5 ms                                                     | 46.1 ms: 1.04x slower                                                       |
| pidigits                 | 149 ms                                                      | 155 ms: 1.04x slower                                                        |
| scimark_fft              | 187 ms                                                      | 197 ms: 1.05x slower                                                        |
| unpickle                 | 9.09 us                                                     | 9.72 us: 1.07x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 104 ms: 1.07x slower                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 70.0 ms: 1.08x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.56 us: 1.10x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 17.1 ms: 1.11x slower                                                       |
| fannkuch                 | 256 ms                                                      | 287 ms: 1.12x slower                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.87 ms: 1.13x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.14 us: 1.14x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 65.8 ms: 1.19x slower                                                       |
| json                     | 3.14 ms                                                     | 3.73 ms: 1.19x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.23 ms: 1.33x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.4 ms: 1.33x slower                                                       |
| coverage                 | 39.0 ms                                                     | 53.9 ms: 1.38x slower                                                       |
| json_loads               | 14.0 us                                                     | 20.5 us: 1.46x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 91.5 ms: 1.47x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.65 ms: 1.88x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): logging_format
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-pythonperf1-amd64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.195x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown