# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-amd64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.231x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.80 sec: 1.06x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 209 ms: 2.08x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 273 ms: 1.93x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 583 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 410 ms: 1.56x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.8 ms: 1.40x faster                                                       |
| float          | 61.7 ms                                                     | 47.7 ms: 1.29x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.2 ms: 1.24x faster                                                       |
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.69x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.45 ms: 1.42x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.6 ms: 1.22x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 95.3 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.19 ms: 1.74x faster                                                       |
| django_template | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 43.9 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.99x faster                                                        |
| async_tree_none          | 435 ms                                                      | 209 ms: 2.08x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 273 ms: 1.93x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 583 ms: 1.90x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.33 ms: 1.79x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.1 us: 1.78x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.19 ms: 1.74x faster                                                       |
| pylint                   | 350 ms                                                      | 207 ms: 1.70x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.69x faster                                                        |
| scimark_sor              | 106 ms                                                      | 64.4 ms: 1.65x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 52.2 ms: 1.64x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.0 ns: 1.63x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.1 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 410 ms: 1.56x faster                                                        |
| go                       | 139 ms                                                      | 89.6 ms: 1.55x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.5 ms: 1.54x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                       |
| pyflate                  | 409 ms                                                      | 285 ms: 1.44x faster                                                        |
| generators               | 32.4 ms                                                     | 22.6 ms: 1.43x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.45 ms: 1.42x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.8 ms: 1.42x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.40x faster                                                       |
| nbody                    | 71.3 ms                                                     | 50.8 ms: 1.40x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 55.4 ms: 1.40x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 871 us: 1.39x faster                                                        |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                        |
| raytrace                 | 273 ms                                                      | 205 ms: 1.33x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.4 ms: 1.31x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                        |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                        |
| float                    | 61.7 ms                                                     | 47.7 ms: 1.29x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 958 ms: 1.27x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 40.2 ms: 1.26x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 472 ms: 1.25x faster                                                        |
| regex_compile            | 106 ms                                                      | 85.2 ms: 1.24x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.6 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| scimark_fft              | 187 ms                                                      | 157 ms: 1.19x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 824 us: 1.16x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 5.03 ms: 1.14x faster                                                       |
| thrift                   | 617 us                                                      | 546 us: 1.13x faster                                                        |
| sympy_sum                | 107 ms                                                      | 94.7 ms: 1.13x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| django_template          | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.80 sec: 1.06x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.5 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.2 ms: 1.05x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 38.3 ms: 1.04x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.61 us: 1.02x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 74.1 ms: 1.02x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.4 ms: 1.02x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 95.3 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.14 us: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| sympy_expand             | 314 ms                                                      | 312 ms: 1.01x faster                                                        |
| fannkuch                 | 256 ms                                                      | 257 ms: 1.01x slower                                                        |
| sqlglot_normalize        | 205 ms                                                      | 211 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 43.9 ms: 1.07x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.40 ms: 1.12x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                       |
| async_generators         | 222 ms                                                      | 266 ms: 1.20x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.6 ms: 1.22x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.86 ms: 1.32x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.1 ms: 1.32x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.231x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown