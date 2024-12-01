# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.303x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                       |
| html5lib       | 94.6 ms                                                      | 71.8 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 332 ms: 2.08x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 406 ms: 2.02x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 840 ms: 1.90x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 572 ms: 1.64x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.5 ms: 1.51x faster                                                        |
| float          | 111 ms                                                       | 82.9 ms: 1.34x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.5 ms: 1.11x faster                                                        |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.18 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 218 us: 1.43x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 336 us: 1.35x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.7 ms: 1.25x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.52 sec: 1.16x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| Geometric mean       | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| django_template | 50.2 ms                                                      | 37.8 ms: 1.33x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.8 ms: 1.13x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.10x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.54 ms: 2.12x faster                                                        |
| async_tree_none          | 692 ms                                                       | 332 ms: 2.08x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 406 ms: 2.02x faster                                                         |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.96x faster                                                        |
| go                       | 262 ms                                                       | 136 ms: 1.93x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 840 ms: 1.90x faster                                                         |
| pylint                   | 566 ms                                                       | 307 ms: 1.84x faster                                                         |
| chaos                    | 109 ms                                                       | 62.2 ms: 1.75x faster                                                        |
| raytrace                 | 489 ms                                                       | 282 ms: 1.74x faster                                                         |
| scimark_lu               | 167 ms                                                       | 96.9 ms: 1.72x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.1 us: 1.71x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.4 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 572 ms: 1.64x faster                                                         |
| logging_silent           | 167 ns                                                       | 103 ns: 1.63x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 66.2 ms: 1.62x faster                                                        |
| deepcopy                 | 468 us                                                       | 294 us: 1.59x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                        |
| richards_super           | 90.6 ms                                                      | 58.2 ms: 1.56x faster                                                        |
| nbody                    | 134 ms                                                       | 88.5 ms: 1.51x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.51x faster                                                        |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.51x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.28 ms: 1.50x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                        |
| pyflate                  | 733 ms                                                       | 499 ms: 1.47x faster                                                         |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.45x faster                                                        |
| richards                 | 75.1 ms                                                      | 51.8 ms: 1.45x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 218 us: 1.43x faster                                                         |
| spectral_norm            | 139 ms                                                       | 100 ms: 1.39x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.37x faster                                                        |
| thrift                   | 1.18 ms                                                      | 859 us: 1.37x faster                                                         |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                         |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 336 us: 1.35x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 141 ms: 1.34x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| float                    | 111 ms                                                       | 82.9 ms: 1.34x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.63 us: 1.34x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.33x faster                                                        |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.24 us: 1.33x faster                                                        |
| django_template          | 50.2 ms                                                      | 37.8 ms: 1.33x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 71.8 ms: 1.32x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                         |
| nqueens                  | 115 ms                                                       | 91.7 ms: 1.25x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.7 ms: 1.25x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.2 ms: 1.25x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 930 us: 1.23x faster                                                         |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                         |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                                         |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.20x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.19x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.7 ms: 1.19x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 68.5 ms: 1.18x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.54 sec: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 59.9 ms: 1.17x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.52 sec: 1.16x faster                                                       |
| scimark_fft              | 361 ms                                                       | 315 ms: 1.15x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 55.8 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.20 ms: 1.13x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.5 ms: 1.11x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.79 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.18 ms: 1.03x slower                                                        |
| async_generators         | 421 ms                                                       | 452 ms: 1.07x slower                                                         |
| telco                    | 7.23 ms                                                      | 8.12 ms: 1.12x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                        |
| coverage                 | 63.3 ms                                                      | 78.5 ms: 1.24x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.95 ms: 1.67x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.20 ms: 1.81x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.40 sec: 219.11x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.303x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.27x