# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.265x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 415 ms: 2.67x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_none         | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 347 ms: 1.84x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.8 ms: 1.38x faster                                                       |
| nbody          | 71.3 ms                                                     | 59.8 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.7 ms: 1.28x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 118 us: 1.55x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.55 ms: 1.40x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.5 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.57 us: 1.06x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.65 us: 1.03x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 17.9 us: 1.04x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.97 us: 1.08x slower                                                       |
| pickle               | 6.85 us                                                     | 7.83 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.5 ms: 1.19x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.34 ms: 1.69x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                       |
| django_template | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 39.1 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.01x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 415 ms: 2.67x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.1 ms: 2.60x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 222 ms: 2.37x faster                                                        |
| async_tree_none          | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 347 ms: 1.84x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 416 ms: 1.76x faster                                                        |
| pylint                   | 350 ms                                                      | 200 ms: 1.76x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.34 ms: 1.69x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.31 sec: 1.62x faster                                                      |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                       |
| go                       | 139 ms                                                      | 86.2 ms: 1.61x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 59.0 ns: 1.60x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.0 ms: 1.58x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 118 us: 1.55x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 19.0 us: 1.51x faster                                                       |
| pyflate                  | 409 ms                                                      | 271 ms: 1.51x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.0 ms: 1.47x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.1 ms: 1.46x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 854 us: 1.42x faster                                                        |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.55 ms: 1.40x faster                                                       |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                      |
| float                    | 61.7 ms                                                     | 44.8 ms: 1.38x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.37x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.0 ms: 1.36x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.28 ms: 1.34x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.9 ms: 1.33x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.6 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.6 ms: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                       |
| regex_compile            | 106 ms                                                      | 82.7 ms: 1.28x faster                                                       |
| pycparser                | 930 ms                                                      | 732 ms: 1.27x faster                                                        |
| scimark_sor              | 106 ms                                                      | 84.3 ms: 1.26x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.52 us: 1.26x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.17 ms: 1.25x faster                                                       |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.22x faster                                                        |
| thrift                   | 617 us                                                      | 506 us: 1.22x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 41.8 ms: 1.21x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 37.0 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.1 ms: 1.20x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.20x faster                                                        |
| nbody                    | 71.3 ms                                                     | 59.8 ms: 1.19x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.18x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.54 sec: 1.16x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 843 us: 1.14x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 58.9 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 529 ms: 1.12x faster                                                        |
| fannkuch                 | 256 ms                                                      | 230 ms: 1.11x faster                                                        |
| django_template          | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.5 ms: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.57 us: 1.06x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 39.1 ms: 1.05x faster                                                       |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 73.7 ms: 1.03x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.65 us: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.03x faster                                                        |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                        |
| logging_format           | 6.76 us                                                     | 6.83 us: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.37 us: 1.02x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 17.9 us: 1.04x slower                                                       |
| async_generators         | 222 ms                                                      | 234 ms: 1.05x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.97 us: 1.08x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 42.9 ns: 1.08x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.47 ms: 1.13x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.83 us: 1.14x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.5 ms: 1.19x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.5 ms: 1.22x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 83.9 ms: 1.35x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.00 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.23 ms: 1.54x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.265x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown