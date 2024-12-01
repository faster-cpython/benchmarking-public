# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-amd64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.162x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 212 ms: 2.05x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 581 ms: 1.91x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 406 ms: 1.57x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.6 ms: 1.09x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 79.3 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| regex_compile  | 106 ms                                                      | 91.5 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.4 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.08 ms: 1.29x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.8 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.2 ms: 1.05x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.53 ms: 1.20x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                       |
| django_template | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                        |
| async_tree_none          | 435 ms                                                      | 212 ms: 2.05x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 581 ms: 1.91x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.90x faster                                                        |
| pylint                   | 350 ms                                                      | 190 ms: 1.84x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 406 ms: 1.57x faster                                                        |
| go                       | 139 ms                                                      | 89.7 ms: 1.55x faster                                                       |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.5 ms: 1.43x faster                                                       |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 67.4 ns: 1.40x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 63.4 ms: 1.35x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.3 us: 1.35x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 919 us: 1.32x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.30x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.8 ms: 1.30x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.08 ms: 1.29x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.1 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 741 ms: 1.26x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.58 ms: 1.25x faster                                                       |
| pyflate                  | 409 ms                                                      | 327 ms: 1.25x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.53 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.7 ms: 1.19x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 809 us: 1.18x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                        |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.8 ms: 1.17x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.0 ms: 1.17x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| scimark_sor              | 106 ms                                                      | 91.6 ms: 1.16x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.5 ms: 1.16x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                       |
| thrift                   | 617 us                                                      | 540 us: 1.14x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| float                    | 61.7 ms                                                     | 56.6 ms: 1.09x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 556 ms: 1.07x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 72.7 ms: 1.06x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.02x faster                                                        |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 94.8 ms: 1.02x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.3 ms: 1.02x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 74.5 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.72 us: 1.01x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.4 ms: 1.00x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.5 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.38 us: 1.03x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.80 ms: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 58.2 ms: 1.05x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| scimark_fft              | 187 ms                                                      | 206 ms: 1.10x slower                                                        |
| nbody                    | 71.3 ms                                                     | 79.3 ms: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| fannkuch                 | 256 ms                                                      | 292 ms: 1.14x slower                                                        |
| coverage                 | 39.0 ms                                                     | 45.6 ms: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.88 ms: 1.24x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 81.7 ms: 1.32x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.87 ms: 1.33x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.162x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown